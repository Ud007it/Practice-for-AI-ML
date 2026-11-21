'''
    Chunk 5: Write NoteBook.save(self) that takes self.notes (a list of Note objects), converts 
    each one back to a dict using the to_dict() you already built, and writes that list of dicts 
    to self.filename with json.dump — same as your Phase 2 save_notes, but now reading from 
    self.notes instead of taking a parameter.
'''


import json

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

    def load(self):
        try:
            with open(self.filename,'r') as f:
                result=json.load(f)
                self.notes = [Note(**item) for item in result]
                return self.notes

        except FileNotFoundError:
            self.notes = []
            return self.notes

        except json.JSONDecodeError:
            print("JSON file is corrupted.")
            self.notes = []
            return self.notes
        
    def save(self):
        note_dicts = [note.to_dict() for note in self.notes]
        with open(self.filename,"w") as f:
            json.dump(note_dicts,f)
    
nb=NoteBook("notes.json")
(nb.load())

n=Note("test","hello",["greet","person"])
nb.notes.append(n)
(nb.save())

print(f"{n.to_dict()}")
