'''
    Chunk A — Install and embed one single word. uv add sentence-transformers
'''

from sentence_transformers import SentenceTransformer

model=SentenceTransformer("all-MiniLM-L6-v2")
vector=model.encode("python")
print(vector)
print(len(vector))