'''
    Chunk 3: Write NoteBook.__init__(self, filename) that stores self.filename = filename and 
    self.notes = [] (empty for now — don’t load yet, that’s the next chunk). Create one NoteBook 
    instance by hand (nb = NoteBook("notes.json")), confirm nb.notes is [] and nb.filename is right.
'''

class Note:
    def __init__(self,title,content,tags):
        self.title=title
        self.content=content
        self.tags=tags
    
    def to_dict(self):
        return {"title":self.title,"content":self.content,"tags":self.tags}
    
class NoteBook:
    def __init__(self,filename):    
        self.filename=filename
        self.notes=[]
    
nb=NoteBook("notes.json")
print(nb.notes)
print(nb.filename)

