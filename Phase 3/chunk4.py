'''
    Chunk 4: Write NoteBook.load(self) that opens self.filename, reads the JSON (list of dicts, 
    same as your old code), and — this is the new part — converts each dict back into a real Note
    object before storing it in self.notes. Since your dict keys (title, content, tags) match
    Note.__init__’s parameter names exactly, you can unpack a dict straight into the constructor
    with Note(**note_dict) — look up what ** does when unpacking a dict into a function call if
    that’s unfamiliar, then use it here. Keep the same FileNotFoundError / JSONDecodeError handling
    you already built in Phase 2 — don’t lose that safety net just because the code moved into a class.
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
    
nb=NoteBook("notes.json")
print(nb.load())
print(nb.notes[0].title)
print(nb.notes[1].title)