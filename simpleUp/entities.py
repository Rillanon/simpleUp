class AuthInfo:

    def __init__(self):
        self.host = None
        self.username = None
        self.password = None

    @staticmethod
    def empty(self):
        if (self.host is None) | (self.username is None) | (self.password is None):
            return True
        else:
            return False