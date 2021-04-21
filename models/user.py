class User():

    def __init__(self, userName, email):
        self._userName = userName
        self._email = email

    def pay_bill(self):
        raise NotImplementedError

    def code(self):
        raise NotImplementedError