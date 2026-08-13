# Minh họa Minimum Viable RAG — xem dev-notes/context-indexing-rag.md mức 1.
# Bản minh họa, cosine similarity thuần (không FAISS). Cài: uv add sentence-transformers faiss-cpu
# extract_functions/extract_imports/cosine_similarity/save_index/read_file cần tự viết thêm.

from sentence_transformers import SentenceTransformer
import os

model = SentenceTransformer('all-MiniLM-L6-v2')


def index_codebase(source_dir):
    """Build semantic index of codebase"""
    index = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(('.py', '.js', '.ts', '.tsx')):
                path = os.path.join(root, file)
                with open(path) as f:
                    content = f.read()
                metadata = {
                    'path': path,
                    'functions': extract_functions(content),
                    'imports': extract_imports(content),
                    'size': len(content)
                }
                embedding = model.encode(content)
                index.append({
                    'metadata': metadata,
                    'embedding': embedding
                })
    return index


def search(query, index, k=5):
    """Find k most relevant files"""
    query_embedding = model.encode(query)
    scores = []
    for item in index:
        score = cosine_similarity(query_embedding, item['embedding'])
        scores.append((score, item['metadata']))
    scores.sort(reverse=True)
    return [metadata for _, metadata in scores[:k]]
