import json

class ToDoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{idx}. {task['task']} [{status}]")

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid index.")

def menu():
    todo = ToDoList()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo.view_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "3":
            todo.view_tasks()
            index = int(input("Enter the task number to mark as completed: ")) - 1
            todo.mark_complete(index)
        elif choice == "4":
            todo.view_tasks()
            index = int(input("Enter the task number to delete: ")) - 1
            todo.delete_task(index)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    menu()
