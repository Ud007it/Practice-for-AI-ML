'''
    Chunk 2: Wrap it in a while True loop with a simple menu (1. Add 2. View 3. Exit) 
    using input(). Test: run it, add two notes through the menu, view them, exit cleanly.

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

notes=[]
while True:
    user=int(input("Choose anything from options:\n1.Add\n2.View\n3.Exit\n\tEnter:"))

    if user==1:
        title=input("Enter title: ")
        content=input("Enter content: ")
        add_note(notes, title,content)
        
    elif user==2:
        print_notes(notes)
    elif user==3:
        print("Thank you! for exiting")
        break
            
  