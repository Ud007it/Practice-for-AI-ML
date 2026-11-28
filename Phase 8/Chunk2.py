'''
    Right now, every time load() runs, it reconstructs Note objects from JSON and — because 
    __init__ always computes the embedding — recomputes every single note's embedding from scratch, 
    every time the app starts. For 5 notes, you won't notice. For 500, you'd be waiting seconds 
    just to run view. We're fixing that by saving the embedding itself, not just the raw text.
    
    Two real problems to solve, think through both before coding:

    to_dict() needs to include the embedding — but self.embedding is a numpy array, and json.dump 
    has no idea how to serialize one (try it without converting first, if you want to see the actual
    TypeError yourself). You already identified the fix conceptually: .tolist() converts it to a 
    plain nested Python list, which json handles natively.
    
    __init__ currently always computes a fresh embedding — but when load() reconstructs a Note from 
    a dict that already has a saved embedding, you don't want to throw that away and recompute it. 
    This means __init__ needs to accept an optional embedding parameter: if one's given (loading 
    from disk), use it directly; if not (a genuinely new note being added), compute it fresh. Look
    up Python's default-parameter syntax (def __init__(self, ..., embedding=None)) and an if embedding 
    is None: check — this is the actual design fork the whole chunk hinges on.
'''



