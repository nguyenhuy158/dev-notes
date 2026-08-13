# Cách gọi index_builder.py — build 1 lần, query nhiều lần.
# Khung sườn minh họa: save_index/read_file chưa định nghĩa, cần tự viết thêm.

from index_builder import index_codebase, search

# Build once
index = index_codebase('./src')
save_index(index, './index/code_embeddings.db')

# Query many times
results = search("session refresh token expiry", index, k=5)
files_to_load = [r['path'] for r in results]

# Send to Claude
context = '\n'.join([read_file(f) for f in files_to_load])
