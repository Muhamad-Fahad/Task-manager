"""
Student Task Manager Application
Author: Fahad Saeed (SP23-BSE-115)
DevOps for Cloud Computing - Lab Assignment 4
"""

from typing import List, Optional


class Task:
    """Represents a single student task."""

    def __init__(self, task_id: int, title: str, completed: bool = False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
        }

    def __repr__(self) -> str:
        status = "Done" if self.completed else "Pending"
        return f"[{self.id}] {self.title} - Status: {status}"


class TaskManager:
    """Manages collection of student tasks."""

    def __init__(self):
        self.tasks: List[Task] = []
        self._next_id: int = 1

    def list_tasks(self) -> List[Task]:
        """Return all managed tasks."""
        return list(self.tasks)

    def display_tasks(self) -> None:
        """Print all tasks formatted to console."""
        if not self.tasks:
            print("No tasks found.")
            return

        print("\n--- Student Task List ---")
        for task in self.tasks:
            print(task)
        print("-------------------------\n")
