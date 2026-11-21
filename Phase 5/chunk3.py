'''
    Chunk 3 — Replace print() with logging. Right now, "Index out of bounds", "Note deleted.",
    "JSON file is corrupted." etc. are all print() calls — fine for a toy script, but real 
    applications separate user-facing output (results the program is designed to show) from 
    diagnostic/error logging (things that help you debug, that a user might not even see). 
    Set up logging.basicConfig(level=logging.INFO) once near the top, then replace your internal
    status/error messages with logging.info(...) or logging.warning(...) / logging.error(...) as
    appropriate — keep the actual note content display (print_notes, search results) as print(),
    since that’s real program output, not a log message. Think about which of your current print() 
    calls are “telling the user something they asked for” versus “telling anyone watching that 
    something went right or wrong internally” — that distinction is the whole point of this chunk.
'''

import argparse
import json

import logging
logging.basicConfig(level=logging.INFO)

class Note:
    def __init__(self, title:str, content:str, tags:list[str]) -> None :
        '''
            Initialize a note with its text and tags for display and storage.
        '''
        
        self.title = title
        self.content = content
        self.tags = tags

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
            "tags": self.tags
        }


class NoteBook:
    def __init__(self, filename:str)-> None:
        '''
            Set the storage filename and initialize the in-memory note list.
        '''
        
        self.filename = filename
        self.notes = []

    def add(self, title:str, content:str, tags:list[str]) -> None:
        '''
            Create and store a note, then save the updated notebook to disk.
        '''
        
        note = Note(title, content, tags)
        self.notes.append(note)
        self.save()

    def delete(self, index:int) -> None:
        '''
            Remove and save the note at this index, or warn if it is out of range.
        '''
        
        if index < 0 or index >= len(self.notes):
            logging.warning("Index out of bounds")
        else:
            del self.notes[index]
            self.save()
            logging.info("Note deleted.")

    def find_by_tag(self, tag:str) -> list[Note]:
        '''
            Return notes containing this exact tag, and report when none match.
        '''
        
        matches = [note for note in self.notes if tag in note.tags]
        if not matches:
            print("No matches tag found.")
        return matches

    def load(self)->None:
        '''
            Load notes from JSON, using an empty list if the file is missing or invalid
        '''
                
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.notes = [Note(**item) for item in data]
        except FileNotFoundError:
            self.notes = []
        except json.JSONDecodeError:
            logging.warning("JSON file is corrupted.")
            self.notes = []

    def save(self)->None:
        '''
            Write the notebook's notes to its JSON file.
        '''
        
        note_dicts = [note.to_dict() for note in self.notes]
        with open(self.filename, "w") as file:
            json.dump(note_dicts, file, indent=4)

    def print_notes(self)->None:
        '''
            Display each note with its list index for viewing or deletion.
        '''
        
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