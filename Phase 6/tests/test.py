'''
    Chunk 2 — Test NoteBook.add() using a temp file, not your real one. Look up pytest’s tmp_path
    fixture — it hands your test function a fresh, throwaway directory that’s automatically cleaned
    up after. Write test_add_creates_note(): create a NoteBook(tmp_path / "test_notes.json"), call 
    .add(...) once, then assert len(nb.notes) == 1 and nb.notes[0].title == "..." matches what you 
    added.
'''
from notevault.storage import NoteBook

def test_add_creates_note(tmp_path):
    nb=NoteBook(tmp_path/"test_notes.json")
    nb.add("Shopping list","Buy apples",["shop"])

    assert len(nb.notes)==1
    assert nb.notes[0].title=="Shopping list"
    