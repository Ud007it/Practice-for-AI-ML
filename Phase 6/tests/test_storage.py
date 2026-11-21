'''
    Chunk 1 — Install and get pytest recognizing one trivial test. uv add pytest --dev (or pip
    install pytest). Create tests/test_storage.py with the single simplest possible test: def 
    test_true(): assert True. Run uv run pytest from Phase 6. Confirm pytest finds and passes it
    before writing anything real — this just proves your tooling and file-discovery (pytest looks 
    for test_*.py files and test_* functions by a naming convention — look that up) are working.
'''

def test_true():
    assert True