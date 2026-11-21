'''
    Chunk 10 — print_notes(): Write NoteBook.print_notes(self) that loops self.notes with enumerate,
    printing index and the note’s fields. Since Note objects don’t print nicely by default 
    (try print(some_note) right now and look at the ugly output you get), you have a choice 
    here: either build the display string manually inside this method using note.title, note.content,
    note.tags, or — better, and worth learning — add a __str__(self) method to the Note class itself
    so print(note) just works cleanly everywhere, not only inside this one method. Try the
    __str__ route; it’s a small, genuinely useful Python concept you haven’t hit yet.
'''


import json

class Note:
    def __init__(self,title,content,tags):
        self.title=title
        self.content=content
        self.tags=tags
        
    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nTags: {self.tags}"
    
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
        matches = []
        for note in self.notes:
            if tag in note.tags:
                matches.append(note)
        if matches == []:
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
            
    def print_notes(self):
        for index,i in enumerate(self.notes):
                print(f"Index: {index}: {i}")
    
# nb = NoteBook("notes.json")
# nb.load()
# results = nb.find_by_tag("oop")  
# for r in results:
#     print(r)

nb = NoteBook("notes.json")
nb.load()

while True:
    print("\n1. Add\n2. View\n3. Delete\n4. Search by Tag\n5. Exit")

    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        title = input("Enter title: ")
        content = input("Enter content: ")
        raw_tags = input("Enter tags separated by commas: ")
        tags = [tag.strip() for tag in raw_tags.split(",") if tag.strip()]
        nb.add(title, content, tags)

    elif choice == 2:
        nb.print_notes()

    elif choice == 3:
        try:
            index = int(input("Enter the note index to delete: "))
        except ValueError:
            print("Please enter a number.")
            continue

        nb.delete(index)

    elif choice == 4:
        tag = input("Search by tag: ").strip()
        matches = nb.find_by_tag(tag)

        for note in matches:
            print(note)

    elif choice == 5:
        print("Thank you for using the notes app!")
        break

    else:
        print("Choose an option from 1 to 5.")