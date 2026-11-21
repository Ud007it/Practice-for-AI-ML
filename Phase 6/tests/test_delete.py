'''
    Chunk 4 — Test delete() and find_by_tag() the same way: add a few notes, delete one by index,
    assert the right one’s gone and the count dropped; search by a tag that exists and one that 
    doesn’t, assert the right lists come back.
    
    Test 1 — delete(): think through what actually needs proving, in two separate cases:

    The success case: add a few notes, delete one by a valid index, assert the right one is
    actually gone — not just that a note is gone, but specifically that the correct note survived.
    (Hint: if you add three notes and delete index 1, check that what remains at index 0 and the
    new index 1 match the notes you expect, by title — don’t just check len() dropped by one,
    since that alone wouldn’t catch “deleted the wrong one.”)
    
    The failure case: call delete() with an index that’s out of range (e.g. 99 on a list of 2 notes).
    What should happen? Look back at your own delete() method — it doesn’t raise an exception for 
    a bad index, it just logs a warning and does nothing. So the test needs to assert that the 
    list is unchanged afterward — same length, same notes — proving the bounds check actually 
    protects the list rather than silently corrupting it.
    
    
    Test 2 — find_by_tag(): same two-case structure:

    Tag exists: add notes with different tags, search for one that’s genuinely present on exactly
    one of them, assert the returned list has the right length and contains the right note (check 
    .title, same as your Chunk 2/3 tests).
    
    Tag doesn’t exist: search for something you know isn’t on any note, assert the returned list
    is empty (assert matches == [] or assert not matches).
'''
from notevault.storage import NoteBook

# def test_delete_removes_correct_note(tmp_path):
#     nb=NoteBook(tmp_path/"test_notes.json")
#     nb.add("Shopping list","Buy apples",["shop"])
#     nb.add("Meeting notes", "Discuss Q4 plans", ["work"])    
#     nb.add("Good morning", "how are you", ['greet']) 
       
#     nb.save()
#     nb.load()
    
   
#     nb.find_by_tag('greet')
    
#     # nb.delete(100)
    
#     assert nb.notes 
#     assert nb.notes[2].tags == ["greet"]
#     # assert nb.notes[100].title == "Good morning"
    



def test_delete_removes_correct_note(tmp_path):
    nb = NoteBook(tmp_path / "test_notes.json")
    nb.add("Shopping list", "Buy apples", ["shop"])
    nb.add("Meeting notes", "Discuss Q4 plans", ["work"])
    nb.add("Good morning", "how are you", ["greet"])

    # delete the MIDDLE note (index 1) — "Meeting notes"
    nb.delete(1)   # <- what index do you pass to remove "Meeting notes" specifically?

    # after deleting index 1, exactly two notes should remain
    assert len(nb.notes) == 2

    # the note that was at index 0 should still be at index 0
    assert nb.notes[0].title == "Shopping list"

    # the note that was at index 2 should have shifted down to index 1
    assert nb.notes[1].title == "Good morning"


def test_delete_out_of_bounds_does_nothing(tmp_path):
    nb = NoteBook(tmp_path / "test_notes.json")
    nb.add("Shopping list", "Buy apples", ["shop"])
    nb.add("Meeting notes", "Discuss Q4 plans", ["work"])

    nb.delete(99)   # <- pick an index that is definitely out of range for a 2-note list

    # if delete() correctly did nothing, how many notes should still be here?
    assert len(nb.notes) == 2

    # and the notes that were already there should be completely unchanged — check at least one
    assert nb.notes[0].title == "Shopping list"
    
def test_find_by_tag_match(tmp_path):
    nb = NoteBook(tmp_path / "test_notes.json")
    nb.add("Shopping list", "Buy apples", ["shop"])
    nb.add("Meeting notes", "Discuss Q4 plans", ["work"])
    nb.add("Good morning", "how are you", ["greet"])

    results = nb.find_by_tag("shop")   # <- pick a tag that matches exactly ONE note above

    assert len(results) == 1
    assert results[0].title == "Shopping list"


def test_find_by_tag_no_match(tmp_path):
    nb = NoteBook(tmp_path / "test_notes.json")
    nb.add("Shopping list", "Buy apples", ["shop"])
    nb.add("Meeting notes", "Discuss Q4 plans", ["work"])

    results = nb.find_by_tag("oop")   # <- pick a tag that exists on NONE of the notes above

    assert results == []