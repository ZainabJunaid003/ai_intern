# To-Do CLI

A small command-line to-do list app written in Python. It uses only the standard library.

## What it does
Lets you add tasks, list them, mark them as done, and delete them. Tasks are saved in a JSON file so they persist between runs.

## Requirements
- Python 3.8 or newer (no extra packages)

## How to run
```
python todo.py add "Buy milk"
python todo.py add "Finish report"
python todo.py list
python todo.py done 1
python todo.py delete 2
```

Example output of `list`:
```
[x] 1. Buy milk
[ ] 2. Finish report
```

## Where data is stored
In `tasks.json` in the folder you run the command from. To use a different file, set the `TODO_FILE` environment variable.

## Run the tests
```
python -m unittest test_todo.py
```

## Project files
- `todo.py` – the app (storage functions + argparse CLI)
- `test_todo.py` – unit tests
