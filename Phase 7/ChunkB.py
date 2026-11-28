'''
    Chunk B — Compare two words. Embed "python" and "coding" separately, then use 
    sentence_transformers.util.cos_sim(vector1, vector2) to get their similarity score. 
    Then embed "python" and "banana" and compare those too. Print both scores side by side.
'''

from sentence_transformers import SentenceTransformer
from sentence_transformers import util

model=SentenceTransformer("all-MiniLM-L6-v2")
vector1=model.encode("python")
vector2=model.encode("coding")

similarity_score=util.cos_sim(vector1,vector2)

print(similarity_score)

vector3 = model.encode("banana")
similarity_score_2 = util.cos_sim(vector1, vector3)
print(similarity_score_2)