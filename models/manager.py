from models.user import User

class Manager(User):

    def __init__(self, userName, email):
        super().__init__(userName, email)

    def pay_bill(self):
        print("paying...")

    def code(self):
        pass