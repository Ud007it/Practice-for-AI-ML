'''
    Chunk 3: Add a delete_note(notes_list, index) function with bounds checking (what if they
    type an index that doesn’t exist?). Test: add 3 notes, delete the middle one, confirm the 
    other two remain.
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
        
def delete_note(notes_list,index):
    if index < 0 or index >= len(notes_list):
        print("Index out of bounds")
    else:
        del notes_list[index]
        print("Note deleted.")
        
notes=[]
while True:
    user=int(input("Choose anything from options:\n1.Add\n2.View\n3.Delete\n4.Exit\n\tEnter:"))

    if user==1:
        title=input("Enter title: ")
        content=input("Enter content: ")
        add_note(notes, title,content)
        
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
        print("Thank you! for exiting")
        break
            
  