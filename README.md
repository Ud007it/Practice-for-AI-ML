# NoteVault

A command-line note-taking app with tagging and search, built in Python. Notes are stored as objects (title, content, tags), persisted to JSON, and fully covered by automated pytest tests.

## Features

- Add, view, delete, and search notes by tag
- Object-oriented design: `Note` and `NoteBook` classes
- Persistent storage via JSON
- Real CLI interface built with `argparse` (subcommands, not a menu)
- Logging for diagnostics, separate from user-facing output
- Automated test suite (pytest) covering add, delete, and search behavior, using isolated temp files so tests never touch real data

## Tech Stack

- **Language:** Python 3.12+
- **Core Libraries:** argparse, json, logging, pytest
- **Tooling:** uv (dependency management), git

## Getting Started

### Prerequisites
- Python 3.12+
- [uv](https://docs.astral.sh/uv/) installed

### Installation

```bash
git clone https://github.com/Ud007it/Practice-for-AI-ML.git
cd Practice-for-AI-ML
uv sync
```

### Usage

All commands run through the CLI module:

```bash
uv run python -m notevault.cli add "Title" "Content" --tags python,urgent
uv run python -m notevault.cli view
uv run python -m notevault.cli search python
uv run python -m notevault.cli delete 0
```

- `add` — creates a note with a title, content, and comma-separated tags
- `view` — lists all notes with their index
- `search <tag>` — returns notes matching that exact tag
- `delete <index>` — removes the note at that index

### Running tests

```bash
uv run pytest -v
```

## What I learned / bugs I fixed

**Shadowed variable instead of function parameter** — An early version of `delete_note` saved the global `notes` list by name instead of the `notes_list` parameter it was actually given. It worked by coincidence because the function always happened to be called with the same global list, but it meant the function secretly depended on program structure instead of its own inputs. Fixed by making every save call use the parameter, never a name reached from outside the function.

**Package import failures from folder naming and structure** — Restructuring the project into a proper `notevault` package broke with `ImportError: attempted relative import with no known parent package`. The actual causes were a folder name containing spaces (invalid in a Python import path) and running scripts from the wrong working directory relative to the package. Fixed by renaming the package folder to a valid identifier and always running commands from the project root using `python -m notevault.cli`.

**A rewritten test file silently deleted a previous test** — While adding a second test to `test_delete.py`, I overwrote the file instead of appending to it, which deleted an already-passing test with no warning — pytest's "passed" count just quietly dropped from one run to the next. Fixed by always appending new test functions to existing test files rather than replacing their contents.

**pytest silently collecting zero tests** — After splitting the project into a package, `pytest` reported `collected 0 items` with no error, because the `tests/` folder had no `__init__.py` and pytest couldn't resolve the `notevault` import path from where it started searching. Fixed by adding an empty `conftest.py` at the project root, which anchors pytest's import path correctly.