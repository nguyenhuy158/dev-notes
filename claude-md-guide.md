# CLAUDE.md viết đúng chuẩn

CLAUDE.md load vào context MỖI request. Dài = tốn token mỗi lần, dù việc đang làm chả liên quan.

## Anti-pattern: nhồi hết vào 1 file

File 4000+ dòng: liệt kê version dependency, giải thích kiến trúc từng service, doc API endpoint, debug guide chi tiết. Model đọc hết nhưng phần liên quan tới task hiện tại chỉ vài %. Tốn token, loãng attention.

## Pattern đúng: tiered — core rules ở CLAUDE.md, chi tiết tách riêng

CLAUDE.md giữ ngắn (~100-200 dòng), chỉ chứa:
- Stack chính (không cần version lẻ)
- Rule bất di bất dịch (never touch X, always do Y)
- Quick reference (auth dùng gì, DB pattern gì, cấu trúc thư mục chính)
- Link trỏ tới doc chi tiết khi cần (`/docs/api-contracts.md`, `/docs/architecture.md`...)

Model chỉ đọc doc chi tiết khi task thật sự cần — không tốn token mặc định.

```
project/
├── CLAUDE.md          # core rules, ngắn
├── docs/
│   ├── api-contracts.md
│   ├── data-models.md
│   ├── debugging.md
│   └── architecture.md
└── .claudeignore
```

## Dấu hiệu file tốt

- Dưới 200 dòng
- Chỉ chứa rule cứng + nguyên tắc kiến trúc, không chi tiết vụn
- Trỏ sang doc chi tiết thay vì nhét thẳng vào
- Mỗi dòng phải xuất hiện relevant trong >10% session — dòng nào ít dùng thì bỏ

## Dấu hiệu file quá to (anti-pattern)

- Hơn 500 dòng
- Chứa full API doc
- Giải thích từng edge case
- Trùng lặp thông tin đã có trong code comment
- Có troubleshooting cho lỗi hiếm gặp

## Checklist viết CLAUDE.md

- Rule cụ thể, action được (never modify migrations/, always write tests) — không viết chung chung kiểu "code sạch"
- Không nhồi version dependency — dễ lỗi thời, model tự đọc package.json lúc cần
- Không giải thích kiến trúc dài dòng — tách sang docs/, chỉ để link
- Ưu tiên bullet ngắn, tránh văn xuôi dài
- Review định kỳ — xóa rule không còn đúng, thêm rule mới học được

Xem thêm cách tổ chức note dùng chung: [README.md](../README.md).
