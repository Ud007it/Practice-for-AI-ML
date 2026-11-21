'''
    Chunk 1: Write just the Note class — __init__(self, title, content, tags) storing those three
    as self.title, self.content, self.tags. Create one Note object by hand in a throwaway test
    line (n = Note("test", "content", ["tag"])), print n.title, confirm it works. Don’t touch the
    rest of the program yet.
'''

class Note:
    def __init__(self,title,content,tags):
        self.title=title
        self.content=content
        self.tags=tags
    
n=Note("test","hello",["greet","person"])
print(f"{n.title} {n.content} {n.tags}")

