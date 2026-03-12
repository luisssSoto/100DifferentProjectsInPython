class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            func(args[0])
    return wrapper

# 1. Approach
@is_authenticated
def create_post(user):
    print(f"The user {user.name} is creating a post")

user1 = User("Alex")
user1.is_logged_in = True
create_post(user1)

# 2. Approach
def create_post2(user):
    print(f"The user {user.name} is creating a post")

user2 = User("Bob")
user2.is_logged_in = True
auth = is_authenticated(create_post2)
auth(user2)

