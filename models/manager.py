from models.user import User

class Manager(User):

    def __init__(self, userName, email):
        super().__init__(userName, email)

    def work(self):
        print("paying...")