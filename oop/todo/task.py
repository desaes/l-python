import datetime

last_id = 0

class Task:
    """Represent a task in the todo. Match against a string in
    searches and store details for each note."""
    
    def __init__(self, title, detail, deadline) -> None:
        self.title = title
        self.detail = detail
        self.deadline = deadline
        self.creation_date = datetime.datetime.today()
        global last_id
        last_id += 1
        self.id = last_id

    def __repr__(self) -> str:
        return f"""Task(id: '{self.id}, \
'tile: '{self.title}', detail: '{self.detail}', \
deadline: {self.deadline}, creation_date: '{self.creation_date}')"""

    def match(self, filter):
        """Determine if this note matches the filter text.
        Return True if it matches, False otherwise.
        
        Search is case sensitive and matches both title and tags."""
        return filter in self.title or filter in self.detail