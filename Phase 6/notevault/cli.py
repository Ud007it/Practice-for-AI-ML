import argparse
import logging
logging.basicConfig(level=logging.INFO)
from .storage import NoteBook


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True)

add_parser = subparsers.add_parser("add")
add_parser.add_argument("title")
add_parser.add_argument("content")
add_parser.add_argument("--tags", default="")

semantic_parser = subparsers.add_parser("search-semantic")
semantic_parser.add_argument("query",type=str)


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
        
elif args.command == "search-semantic":
    matches = nb.semantic_search(args.query) 
    for note in matches:
        print(note)
        
    