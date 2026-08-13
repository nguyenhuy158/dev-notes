# Context indexing / RAG cho AI coding agent

Nguồn: bài "How to Hyper-Optimise Claude Code" (dev.to/andrei_nita), mục #7
"Context Indexing + RAG: 40-90% Token Reduction". Ghi lại để project sau cân
nhắc trước khi tự dựng RAG — thường **chưa cần** tới mức đó.

## Vấn đề

CLAUDE.md/dev-notes phình to → mỗi request agent nạp hết vào context, tốn
token dù phần lớn không liên quan task hiện tại.

## Ý tưởng chính

Đừng nhồi hết tài liệu vào CLAUDE.md. Giữ file gốc **lean** (mục lục + link ra
file chi tiết — pattern `dev-notes/` đang dùng), chi tiết sâu chỉ đọc **khi
cần** (agent tự tìm đúng phần, không nạp sẵn toàn bộ).

## 3 mức áp dụng, từ nhẹ tới nặng

### Mức 0 — progressive disclosure (đang dùng ở đây)

Mục lục + file con trỏ trong `dev-notes/`, `CLAUDE.md` chỉ link tới file cần.
Không index, không embedding. Đủ khi số file docs còn ít (chục file) — agent
tự grep/đọc đúng tên file là ra.

### Mức 1 — Minimum Viable RAG (`all-MiniLM-L6-v2`)

Dùng khi số file/docs nhiều lên tới mức grep theo tên không còn ăn (câu hỏi
không khớp từ khoá, hoặc cần tìm theo *ý nghĩa*).

```
project/
├── src/                        # code/docs gốc, không đụng vào
└── index/
    └── embeddings.db            # vector nhỏ, sinh bằng all-MiniLM-L6-v2
                                  # (model 384-dim, nhẹ, chạy local/CPU, free)
```

Chỉ 1 bước: chunk file → embed bằng MiniLM → lưu vector db nhẹ (sqlite +
sqlite-vec, hoặc Chroma local). Query = embed câu hỏi, cosine similarity lấy
top-k chunk, nhồi vào prompt. Không cần metadata phức tạp hay dependency
graph — đây là lý do gọi "minimum viable".

Script minh họa: [`rag-scripts/index_builder.py`](rag-scripts/index_builder.py)
(build index) và [`rag-scripts/usage_example.py`](rag-scripts/usage_example.py)
(cách gọi). Đây là **khung sườn, chưa chạy được ngay** — thiếu
`extract_functions`/`extract_imports`/`cosine_similarity`/`save_index`/
`read_file`, phải tự viết thêm. Cài bằng `uv add sentence-transformers
faiss-cpu` (faiss optional, chỉ cần khi index lớn). Build index 1 lần, query
nhiều lần.

### Mức 2 — full index architecture

Kiến trúc đầy đủ trong bài gốc, cho codebase lớn:

```
project/
├── src/                         # 2,847 files, 3.4M tokens
├── index/
│   ├── code_embeddings.db       # vector search (như mức 1, nhưng full-repo)
│   ├── file_metadata.json       # tra cứu nhanh: path, size, last-modified...
│   └── dependency_graph.json    # quan hệ import/reference giữa file
└── .claude/
    └── retrieval_config.json    # cấu hình: model embedding, top-k,
                                  # rule khi nào dùng index vs đọc trực tiếp
```

Thêm 2 lớp so với mức 1:

- **metadata**: lọc nhanh theo file/loại trước khi vector search, đỡ phải
  embed lại.
- **dependency graph**: trả lời được "file nào import X" — quan hệ cấu trúc
  code không nằm trong ngữ nghĩa câu chữ, thuần vector search không làm tốt.

Đáng làm khi codebase cỡ hàng nghìn file/vài triệu token, nhiều agent/nhiều
người cùng tra cứu lâu dài — chi phí duy trì index (rebuild khi code đổi) mới
bù lại được.

## Chọn mức nào cho personal-projects

Quy mô hiện tại (vài project nhỏ + vài chục file dev-notes) → **mức 0 là đủ**.
Nếu dev-notes phình to và agent bắt đầu tra sai/chậm, nâng lên **mức 1** trước
(rẻ, dễ làm, không cần metadata/dependency graph). Chỉ nhảy thẳng lên mức 2 khi
có 1 codebase lớn thật (nghìn file) cần tra cứu quan hệ code, không phải chỉ
tra docs.

## Khi nào nên nâng cấp lên RAG thật

Dấu hiệu: số file docs quá lớn, tìm bằng grep/Explore agent không ra đúng chỗ,
nhiều project cùng cần tra 1 nguồn tri thức lớn. Nếu muốn tự làm trên
Cloudflare (Vectorize + Workers AI cho embedding), xem skill `agents-sdk` /
`cloudflare` — có sẵn hướng dẫn build RAG pipeline trên nền đó.
