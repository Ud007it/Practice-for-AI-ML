'''
    Chunk 3 — Test that save/load round-trips correctly, using the same tmp_path pattern:
    add two notes, save, create a second NoteBook instance pointed at the same temp file, load 
    it, assert the titles match. This is the exact manual test you did by hand back in Phase 3
    — now automated and safe to run a thousand times without touching real data.
'''

from notevault.storage import NoteBook

def test_add_creates_note(tmp_path):
    nb=NoteBook(tmp_path/"test_notes.json")
    nb.add("Shopping list","Buy apples",["shop"])
    nb.add("Meeting notes", "Discuss Q4 plans", ["work"])    
    
    nb1=NoteBook(tmp_path/"test_notes.json")
    nb1.load()
    
    assert nb1.notes
    assert len(nb1.notes) == 2
    assert nb1.notes[0].title == "Shopping list"
    assert nb1.notes[1].title == "Meeting notes"
    