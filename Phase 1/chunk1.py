'''
    Chunk 1: Write a function add_note(notes_list, title, content) that appends a dict to a list,
    and a print_notes(notes_list) that loops through and prints them.
    Test: call add_note twice,call print_notes, see both show up.
'''

def add_note(notes_list, title, content):
    print_dict={
        "title":title,
        "content":content
    }
    notes_list.append(print_dict)

def print_notes(notes_list):
    for i in notes_list:
        print(i)
        
notes = []

add_note(notes, "Shopping", "Buy milk and bread")
add_note(notes, "Reminder", "Call Sam")

print_notes(notes)