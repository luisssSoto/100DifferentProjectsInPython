class User:
    def __init__(self, id, user_name):
        self.id = id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Alex")
print(user_1.id)
print(user_1.user_name)
print(user_1.followers)

user_2 = User("002", "Alexa")
print(user_2.id)
print(user_2.user_name)
print(user_2.followers)
print()

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)

