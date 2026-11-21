'''
   Chunk 6: Full round-trip test: create a fresh NoteBook, manually append two Note objects to
   nb.notes (no add() method yet, just append by hand for this test), call nb.save(), then create 
   a second, separate NoteBook instance pointing at the same file, call .load() on it, and print
   the titles. Do the two notes survive the round trip intact? 
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

n1=Note("hello","test1",["testing","code"])
n2=Note("hi","test2",["class","oop"])
nb.notes.append(n1)
nb.notes.append(n2)
(nb.save())

loaded_nb=NoteBook("notes.json")
(loaded_nb.load())
for note in loaded_nb.notes:
    print(note.title)
