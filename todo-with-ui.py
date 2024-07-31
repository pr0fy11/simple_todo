import os
#файл към променлива
TODO_FILE = 'todo.txt'
#конструктор 
class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        status = " (completed)" if self.completed else ""
        return self.description + status
#основни функционалности на програмата
class ToDoList:
    def __init__(self):
        self.tasks = self.load_tasks()
#проверка дали файлът съществува. Отваряме файла с read, създаваме списък. За всяка лининя във файла която завършва с completed прибавяме в списъка tasks -12 първите реда които са описанинето и сетва статуса нан true
    def load_tasks(self):
        if not os.path.exists(TODO_FILE):
            return []
        with open(TODO_FILE, 'r') as file:
            tasks = []
            for line in file:
                line = line.strip()
                if line.endswith(" (completed)"):
                    tasks.append(Task(line[:-12], True))
                else:
                    tasks.append(Task(line))
        return tasks

    def save_tasks(self):
        with open(TODO_FILE, 'w') as file:
            for task in self.tasks:
                file.write(str(task) + '\n')

    def add_task(self, description):
        self.tasks.append(Task(description))
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
# метод за маркиране на завършена задача. Проверка дали задачата съществува, 
    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = True
            self.save_tasks()
            print(f"Marked task {task_number} as completed.")
        else:
            print("Invalid task number.")
#menu
def show_menu():
    print("\nTo-Do List App")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as completed")
    print("5. Exit")

def main():
    todo_list = ToDoList()

    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            description = input("Enter a new task: ")
            todo_list.add_task(description)
        elif choice == '3':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                todo_list.mark_task_completed(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
