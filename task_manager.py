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

    def add_task(self, title: str) -> Task:
        """
        Add a new task with non-empty title validation.
        Raises ValueError if title is empty or only whitespace.
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or blank.")

        sanitized_title = title.strip()
        new_task = Task(task_id=self._next_id, title=sanitized_title, completed=False)
        self.tasks.append(new_task)
        self._next_id += 1
        return new_task

    def complete_task(self, task_id: int) -> Task:
        """
        Mark an existing task as completed using its task_id.
        Raises ValueError if task_id does not exist.
        """
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return task
        raise ValueError(f"Task with ID {task_id} not found.")

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
