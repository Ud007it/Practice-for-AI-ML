from sentence_transformers import SentenceTransformer
from sentence_transformers import util
import numpy as np
model=SentenceTransformer("all-MiniLM-L6-v2")


class Note:
    def __init__(self, title:str, content:str, tags:list[str],embedding=None) -> None :
        '''
            Initialize a note with its text and tags for display and storage.
        '''
        
        self.title = title
        self.content = content
        self.tags = tags
        
        if embedding is None:
    # Situation A — nobody gave us one, so compute it fresh   
            full_text = f"{title} {content}"
            self.embedding = model.encode(full_text)
        else:
    # Situation B — one was already provided, just use it
           self.embedding = np.array(embedding, dtype=np.float32)
        

    def __str__(self)-> str:
        '''
            Format the note's fields as readable text for users.
        '''
        
        return f"Title: {self.title}\nContent: {self.content}\nTags: {self.tags}"

    def to_dict(self) -> dict:
        '''
            Convert the note to JSON-compatible data so it can be saved
        '''
        
        return {
            "title": self.title,
            "content": self.content,
            "tags": self.tags,
            "embedding":self.embedding.tolist(),
        }

