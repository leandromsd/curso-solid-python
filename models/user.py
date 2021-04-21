class User():

    def __init__(self, userName, email):
        self._userName = userName
        self._email = email

    @staticmethod
    def members():
        return ['username1', 'username2', 'username3']
