
def show_menu():
    """Displays the interactive menu options."""
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(todo_list):
    """Displays all current tasks with their status."""
    if not todo_list:
        print("\nYour to-do list is empty! 🎉")
        return
    
    print("\nYOUR TASKS:")
    for index, item in enumerate(todo_list, start=1):
        status = "✅ Completed" if item["completed"] else "⏳ Pending"
        print(f"{index}. {item['task']} [{status}]")

def add_task(todo_list):
    """Prompts user to type a new task and adds it to the list."""
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        todo_list.append({"task": task_name, "completed": False})
        print(f"'{task_name}' has been added successfully!")
    else:
        print("Task description cannot be empty.")

def mark_completed(todo_list):
    """Marks a selected task as completed based on its index."""
    view_tasks(todo_list)
    if not todo_list:
        return

    try:
        choice = int(input("\nEnter the number of the task you completed: "))
        if 1 <= choice <= len(todo_list):
            todo_list[choice - 1]["completed"] = True
            print(f"Great job! '{todo_list[choice - 1]['task']}' is marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(todo_list):
    """Removes a selected task from the list."""
    view_tasks(todo_list)
    if not todo_list:
        return

    try:
        choice = int(input("\nEnter the number of the task to delete: "))
        if 1 <= choice <= len(todo_list):
            removed = todo_list.pop(choice - 1)
            print(f"Deleted task: '{removed['task']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main program execution loop."""
    # Tasks are stored as a list of dictionaries tracking names and completion status
    todo_list = []
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == "1":
            view_tasks(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            print("\nGoodbye! Stay productive! 🚀")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
