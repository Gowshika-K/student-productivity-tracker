import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, t in enumerate(tasks, start=1):
        status = "✔" if t["completed"] else "✘"
        print(f"{idx}. [{status}] {t['task']}")

def complete_task(tasks):
    view_tasks(tasks)
    choice = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= choice < len(tasks):
        tasks[choice]["completed"] = True
        save_tasks(tasks)
        print("Marked task as completed!")
    else:
        print("Invalid choice!")

def delete_task(tasks):
    view_tasks(tasks)
    choice = int(input("Enter task number to delete: ")) - 1
    if 0 <= choice < len(tasks):
        removed = tasks.pop(choice)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid choice!")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- Task Tracker ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
