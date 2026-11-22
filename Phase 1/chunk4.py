'''
    Chunk 4: Add tags (a list of strings) to each note, and a find_by_tag(notes_list, tag)
    function. Test: add notes with different tags, search one tag, confirm only matching 
    notes return.
'''


def add_note(notes_list, title, content,tags):
        note={
            "title":title,
            "content":content,
            "tags":tags
        }
        notes_list.append(note)

def print_notes(notes_list):
    for index,i in enumerate(notes_list):
        print(f"Index: {index}: {i}")
        
def delete_note(notes_list,index):
    if index < 0 or index >= len(notes_list):
        print("Index out of bounds")
    else:
        del notes_list[index]
        print("Note deleted.")
    
def find_by_tag(notes_list, tag):
    matches=[]
    for note in notes_list:
        if tag in note["tags"]:
            matches.append(note)
    if matches==[]:
        print("No matches tag found.")
    return matches

       
notes=[]
while True:
    try:
        user=int(input("Choose anything from options:\n1.Add\n2.View\n3.Delete\n4.Search by Tag\n5.Exit\n\tEnter:"))
    
    except ValueError:
        print("Please enter a number.")
        continue

    if user==1:
        title=input("Enter title: ")
        content=input("Enter content: ")
        # tag=(input("Name a tag to it: ").strip())
        raw_tags = input("Enter tags separated by commas: ")
        tag = [part.strip() for part in raw_tags.split(",") if part.strip()]
        add_note(notes, title,content,tag)
            
    elif user==2:
            print_notes(notes)
            
    elif user==3:
        try:
            index = int(input("Enter the index of the note to delete: "))
        except ValueError:
            print("Please enter a number.")
            continue

        delete_note(notes, index)
            
    elif user==4:
        search=input("Search by Tag: ").strip()
        found_tags=find_by_tag(notes,search)
        print_notes(found_tags)
            
    elif user==5:
        print("Thank you! for exiting")
        break
                
  