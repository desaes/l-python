from task import Task

class Todo:
    def __init__():
        self.task_list = []

    def create_task(self, title):
        task = task(title)
        self.task_list.append(task)

    def search_task_by_id(self, id):
        for task in self.task_list:
            if task.id == id:
                return task
                break

    def search_task_by_title(self, title):
        return [task for task in self.tasks if title in task.title]

    
    
