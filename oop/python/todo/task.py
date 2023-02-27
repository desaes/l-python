class Task:
    id = 0
    def __init__(title):
        global id
        id += 1
        self.id = id
        self.title = title

    def modify_title(self, title):
        self.title = title

