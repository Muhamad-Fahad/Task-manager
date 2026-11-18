"""
Main CLI entrypoint for Student Task Manager.
Author: Fahad Saeed (SP23-BSE-115)
"""

import sys
from task_manager import TaskManager


def show_menu():
    print("\n===============================")
    print("   STUDENT TASK MANAGER CLI   ")
    print("===============================")
    print("1. View All Tasks")
    print("2. Add New Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("===============================")


def run_cli():
    manager = TaskManager()
    print("Welcome to Student Task Manager!")

    while True:
        show_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            manager.display_tasks()
        elif choice == "2":
            title = input("Enter task title: ")
            try:
                task = manager.add_task(title)
                print(f"[SUCCESS] Task added successfully: ID={task.id}, Title='{task.title}'")
            except ValueError as err:
                print(f"[VALIDATION ERROR] {err}")
        elif choice == "3":
            raw_id = input("Enter task ID to mark as completed: ").strip()
            try:
                task_id = int(raw_id)
                task = manager.complete_task(task_id)
                print(f"[SUCCESS] Task marked as completed: ID={task.id}, Title='{task.title}', Status=Done")
            except ValueError as err:
                print(f"[ERROR] Invalid input or task ID: {err}")
        elif choice == "4":
            if hasattr(manager, "delete_task"):
                task_id_str = input("Enter task ID to delete: ").strip()
                try:
                    task_id = int(task_id_str)
                    task = manager.delete_task(task_id)
                    print(f"Task deleted successfully: {task}")
                except (ValueError, KeyError) as err:
                    print(f"Error: {err}")
            else:
                print("Feature 'delete-task' is under active development.")
        elif choice == "5":
            print("Exiting Student Task Manager. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid selection. Please choose an option between 1 and 5.")


if __name__ == "__main__":
    run_cli()
