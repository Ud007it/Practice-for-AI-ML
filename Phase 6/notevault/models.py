
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

