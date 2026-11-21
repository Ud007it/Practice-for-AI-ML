'''
    Chunk 7 — add(): Write NoteBook.add(self, title, content, tags) that builds a Note from 
    those arguments, appends it to self.notes, and calls self.save() — mirroring exactly what your 
    old add_note + manual save_notes call used to do, but now the method owns both steps itself 
    instead of the while loop remembering to do them separately.
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
    
    def add(self, title, content, tags):
        add_notes = Note(title, content, tags)
        self.notes.append(add_notes)
        self.save()

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
