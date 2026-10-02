#!/usr/bin/env python3
"""A small command-line to-do app. Tasks are stored in a JSON file."""

import argparse
import json
import os
import sys

DEFAULT_FILE = os.environ.get("TODO_FILE", "tasks.json")


def load_tasks(path=DEFAULT_FILE):
    """Read tasks from the JSON file. Return an empty list if it doesn't exist."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, path=DEFAULT_FILE):
    """Write the task list to the JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, title):
    """Add a new task with the next free id and return it."""
    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": next_id, "title": title, "done": False}
    tasks.append(task)
    return task


def mark_done(tasks, task_id):
    """Mark a task as done. Return True if found, else False."""
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            return True
    return False


def delete_task(tasks, task_id):
    """Remove a task by id. Return True if something was removed."""
    before = len(tasks)
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    return len(tasks) < before


def build_parser():
    parser = argparse.ArgumentParser(description="Simple to-do list manager")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="add a new task")
    p_add.add_argument("title", help="task description")

    sub.add_parser("list", help="show all tasks")

    p_done = sub.add_parser("done", help="mark a task as done")
    p_done.add_argument("id", type=int)

    p_del = sub.add_parser("delete", help="delete a task")
    p_del.add_argument("id", type=int)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    tasks = load_tasks()

    if args.command == "add":
        task = add_task(tasks, args.title)
        save_tasks(tasks)
        print(f"Added task {task['id']}: {task['title']}")
    elif args.command == "list":
        if not tasks:
            print("No tasks yet.")
        for t in tasks:
            mark = "x" if t["done"] else " "
            print(f"[{mark}] {t['id']}. {t['title']}")
    elif args.command == "done":
        if mark_done(tasks, args.id):
            save_tasks(tasks)
            print(f"Task {args.id} marked as done.")
        else:
            print(f"Task {args.id} not found.")
            return 1
    elif args.command == "delete":
        if delete_task(tasks, args.id):
            save_tasks(tasks)
            print(f"Task {args.id} deleted.")
        else:
            print(f"Task {args.id} not found.")
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
