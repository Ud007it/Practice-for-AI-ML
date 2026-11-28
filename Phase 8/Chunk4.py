'''
    Chunk 4 — Wire it into the CLI

    Last piece of Phase 9. Add a new subcommand, search-semantic, alongside your existing exact-match 
    search — in cli.py:

    Argparse side: add a new subparser, same pattern as your other four: semantic_parser = 
    subparsers.add_parser("search-semantic"), with a positional query argument (a full phrase, so 
    think about whether argparse needs any special handling for multi-word input without quotes —
    test search-semantic find my python notes unquoted and see what happens, versus search-semantic
    "find my python notes" quoted, before deciding if there's an issue to solve).
    
    Dispatch side: elif args.command == "search-semantic": matches = nb.semantic_search(args.query);
    for note in matches: print(note) — same shape as your existing search dispatch, just calling the
    new method.
'''
