import os
import tempfile
import unittest

import todo


class TodoTests(unittest.TestCase):
    def test_add_assigns_incrementing_ids(self):
        tasks = []
        a = todo.add_task(tasks, "first")
        b = todo.add_task(tasks, "second")
        self.assertEqual((a["id"], b["id"]), (1, 2))

    def test_mark_done(self):
        tasks = []
        todo.add_task(tasks, "x")
        self.assertTrue(todo.mark_done(tasks, 1))
        self.assertTrue(tasks[0]["done"])
        self.assertFalse(todo.mark_done(tasks, 99))

    def test_delete(self):
        tasks = []
        todo.add_task(tasks, "x")
        self.assertTrue(todo.delete_task(tasks, 1))
        self.assertEqual(tasks, [])
        self.assertFalse(todo.delete_task(tasks, 1))

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "t.json")
            tasks = []
            todo.add_task(tasks, "persist me")
            todo.save_tasks(tasks, path)
            self.assertEqual(todo.load_tasks(path), tasks)

    def test_load_missing_file_returns_empty(self):
        self.assertEqual(todo.load_tasks("does_not_exist.json"), [])


if __name__ == "__main__":
    unittest.main()
