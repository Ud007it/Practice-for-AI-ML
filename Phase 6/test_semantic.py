from notevault.storage import NoteBook

nb = NoteBook("notes.json")
nb.load()

results = nb.semantic_search("Programming", top_n=2)
print(f"Number of results: {len(results)}")

for note in results:
    print(note)