import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter priority (High / Medium / Low): ")

    task = {
        "title": title,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(
            f"{index}. {task['title']} | Priority: {task['priority']} | Status: {status}"
        )


def mark_task_completed(tasks):
    view_tasks(tasks)
    choice = int(input("Enter task number to mark as completed: ")) - 1

    if 0 <= choice < len(tasks):
        tasks[choice]["completed"] = True
        save_tasks(tasks)
        print("✅ Task marked as completed!")
    else:
        print("❌ Invalid task number")


def delete_task(tasks):
    view_tasks(tasks)
    choice = int(input("Enter task number to delete: ")) - 1

    if 0 <= choice < len(tasks):
        tasks.pop(choice)
        save_tasks(tasks)
        print("🗑️ Task deleted!")
    else:
        print("❌ Invalid task number")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- Student Productivity & Task Tracker ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
