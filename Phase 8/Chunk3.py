'''
    Chunk 3 — NoteBook.semantic_search(query, top_n=3)

    This is the payoff chunk — the one that turns all this embedding plumbing into an actual usable 
    feature. Walk through the pieces before coding:

    What the method needs to do, in order:

    Embed the incoming query string the same way notes get embedded — one call to model.encode(query).
    For every note in self.notes, compute the similarity between the query's embedding and that note's 
    self.embedding, using util.cos_sim — same function you already used in Chunk B to compare "python" 
    vs "coding".
    Sort all notes by that similarity score, highest first.
    Return only the top top_n of them.
'''
