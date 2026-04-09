"""
A simple to-do list application
"""

def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 40)
    print("TO-DO LIST APPLICATION")
    print("=" * 40)
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Exit")
    print("=" * 40)

def add_task(tasks):
    """Add a new task to the list"""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"✓ Task '{task}' added successfully!")
    else:
        print("Task cannot be empty.")

def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour Tasks:")
        print("-" * 40)
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("-" * 40)

def remove_task(tasks):
    """Remove a task from the list"""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"✓ Task '{removed}' removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the to-do list app"""
    tasks = []
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Thank you for using To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
