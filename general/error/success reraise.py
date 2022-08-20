class User:
    def __init__(self, name, engagement) -> None:
        self.name = name
        self.engament_metrics = engagement
        self.score = 0

    def __repr__(self):
        return f'<User {self.name}>'

def get_user_score(user):
    try:
        my_user.score = perform_calculation(user.engament_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function')
        raise # reraise and crashs the program. Must be used inside the except block
    else: # this is the on success
        if user.score > 500:
            send_notification(self.name)

def send_notification(user):
    pass

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_engagement_notification(user):
    print(f'Notification sent to {user}.')

my_user = User('Rolf', {'clicks': 61, 'hits': 100})
get_user_score(my_user)