# Simple Task Manager in Python
# Beginner-friendly project for GitHub

tasks = []

def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "✓" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['task']}")

def complete_task():
    view_tasks()
    if tasks:
        choice = int(input("Enter task number to mark as complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice-1]["done"] = True
            print(f"Task '{tasks[choice-1]['task']}' marked as complete!")
        else:
            print("Invalid task number.")

def delete_task():
    view_tasks()
    if tasks:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice-1)
            print(f"Task '{removed['task']}' deleted!")
        else:
            print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
