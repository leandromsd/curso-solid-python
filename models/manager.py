from models.user import User

class Manager(User):

    def __init__(self, userName, email):
        super().__init__(userName, email)

    @staticmethod
    def members():
        raise Exception("Member is not authorized to the this!")