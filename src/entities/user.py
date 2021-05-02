class User:
    def __init__(self, username, password, user_id = None):
        self.username = username
        self.password = password
        self.user_id = user_id

    def set_user_id(self, id):
        self.user_id = id