'''
    Chunk 9 — find_by_tag(): Write NoteBook.find_by_tag(self, tag) returning a list of matching
    Note objects from self.notes — same logic as before, just operating on self.notes instead of
    a passed-in parameter.
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
        
    def delete(self, index):
        if index < 0 or index >= len(self.notes):
                print("Index out of bounds")
        else:
            del self.notes[index]
            self.save()
            print("Note deleted.")

    def find_by_tag(self, tag):
        matches=[]
        for note in self.notes:
            if tag in self.notes[tag]:
                matches.append(note)
        if matches==[]:
            print("No matches tag found.")
        return matches
    
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
