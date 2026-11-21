import argparse
import json

import logging
logging.basicConfig(level=logging.INFO)
from .models import Note

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
