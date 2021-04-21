from models.user import User

class Member(User):

    def __init__(self, userName, email):
        super().__init__(userName, email)

    @staticmethod
    def members():
        return ['username1', 'username2', 'username3']

    def work(self):
        print("coding...")