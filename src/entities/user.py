class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_id = None

    def set_user_id(self, id):
        self.user_id = id