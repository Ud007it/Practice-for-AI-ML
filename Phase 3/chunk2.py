'''
    Chunk 2: Add a to_dict(self) method on Note that returns {"title": ..., "content": ..., "tags": ...}
    — you need this because json.dump can serialize a plain dict, but it has no idea how to serialize
    a custom object. Test: create a Note, call .to_dict(), confirm it matches the shape your old code 
    used to build manually.

'''


class Note:
    def __init__(self,title,content,tags):
        self.title=title
        self.content=content
        self.tags=tags
    
    def to_dict(self):
        return {"title":self.title,"content":self.content,"tags":self.tags}
    
n=Note("test","hello",["greet","person"])
# print(f"{n.title} {n.content} {n.tags}")
print(f"{n.to_dict()}")

