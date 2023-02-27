import todo import Todo

class Menu:
    def __init__(self) -> None:
        todo = Todo()

    def display_menu(self):
        print('''
        1 ) Add a task
        2 ) Search a task by title
        4 ) Modify a task by id
        ''')