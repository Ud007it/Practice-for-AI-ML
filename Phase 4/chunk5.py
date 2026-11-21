'''
    Chunk 5: Delete the entire while True menu loop. It’s not needed anymore — the whole point of 
    this phase is that the script does one thing per run and exits, driven by what you typed on 
    the command line.
'''


import argparse
import json


class Note:
    def __init__(self, title, content, tags):
        self.title = title
        self.content = content
        self.tags = tags

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nTags: {self.tags}"

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "tags": self.tags
        }


class NoteBook:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []

    def add(self, title, content, tags):
        note = Note(title, content, tags)
        self.notes.append(note)
        self.save()

    def delete(self, index):
        if index < 0 or index >= len(self.notes):
            print("Index out of bounds")
        else:
            del self.notes[index]
            self.save()
            print("Note deleted.")

    def find_by_tag(self, tag):
        matches = [note for note in self.notes if tag in note.tags]
        if not matches:
            print("No matches tag found.")
        return matches

    def load(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.notes = [Note(**item) for item in data]
        except FileNotFoundError:
            self.notes = []
        except json.JSONDecodeError:
            print("JSON file is corrupted.")
            self.notes = []

    def save(self):
        note_dicts = [note.to_dict() for note in self.notes]
        with open(self.filename, "w") as file:
            json.dump(note_dicts, file, indent=4)

    def print_notes(self):
        for index, note in enumerate(self.notes):
            print(f"Index: {index}\n{note}")


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True)

add_parser = subparsers.add_parser("add")
add_parser.add_argument("title")
add_parser.add_argument("content")
add_parser.add_argument("--tags", default="")

subparsers.add_parser("view")

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("index",type=int)

search_parser = subparsers.add_parser("search")
search_parser.add_argument("tag")

args = parser.parse_args()

nb = NoteBook("notes.json")
nb.load()

if args.command == "add":
    tags = [tag.strip() for tag in args.tags.split(",") if tag.strip()]
    nb.add(args.title, args.content, tags)
    print(f"Added note: {args.title}")

elif args.command == "view":
    nb.print_notes()

elif args.command == "delete":
    nb.delete(args.index)

elif args.command == "search":
    matches = nb.find_by_tag(args.tag)
    for note in matches:
        print(note)