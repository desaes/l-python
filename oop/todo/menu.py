from todo import Todo
import sys

class Menu:
    def __init__(self) -> None:
        self.todo = Todo()
        self.choices = {
            "1": self.show_tasks,
            "2": self.search_tasks,
            "3": self.add_task,
            "4": self.modify_task,
            "5": self.quit,
        }

    def display_menu(self):
        print(
            f"""
Todo Menu
1. Show all Tasks
2. Search Tasks
3. Add Tasks
4. Modify Task
5. Quit
        """)
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def show_tasks(self, tasks=None):
        if not tasks:
            tasks = self.todo.tasks
        if len(tasks) > 0:
            for task in tasks:
                print(task)
        else:
            print("Task not found.")

    def search_tasks(self):
        filter = input("Search for: ")
        tasks = self.todo.search_task(filter)
        self.show_tasks(tasks)

    def add_task(self):
        title = input("Enter a title: ")
        detail = input("Enter detail: ")
        deadline = input("Enter the deadline: ")
        self.todo.create_task(title, detail, deadline)
        print("Task has been added.")
    
    def modify_task(self):
        id = input("Enter the task id: ")
        if self.todo.find_task(id):
            title = input("Enter a new title: ")
            detail = input("Enter a new detail: ")
            deadline = input("Enter a new deadline: ")
            if title:
                self.todo.modify_task_title(id, title)
            if detail:
                self.todo.modify_task_detail(id, detail)
            if deadline:
                self.todo.modify_task_deadline(id, deadline)
        else:
            print("Task id not found.")

    def quit(self):
        print("Thank you")
        sys.exit(0)
        
if __name__ == "__main__":
    menu = Menu()
    menu.run()
