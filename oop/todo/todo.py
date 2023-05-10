from task import Task

class Todo:

    def __init__(self) -> None:
        self.tasks = []

    def find_task(self, task_id):
        for task in self.tasks:
            if str(task.id) == task_id:
                return task
        return None

    
    def create_task(self, title, detail, deadline):
        """Creates a new task and append it to tasks list"""
        self.tasks.append(Task(title=title, detail=detail, deadline=deadline))

    def modify_task_title(self, task_id, new_task_title):
        self.find_task(task_id).title = new_task_title

    def modify_task_detail(self, task_id, new_task_detail):
        self.find_task(task_id).detail = new_task_detail

    def modify_task_deadline(self, task_id, new_task_deadline):
        self.find_task(task_id).deadline = new_task_deadline

    def search_task(self, filter):
        return [task for task in self.tasks if task.match(filter)]

"""
if __name__ == "__main__":
    todo = Todo()
    todo.create_task('test','test task', 1)
    todo.modify_task(1, 'new test', 'new detail')
    print(todo.search_task('test'))
"""