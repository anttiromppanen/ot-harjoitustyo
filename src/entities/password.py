class Password:
    def __init__(self, username, password, site):
        self.username = username
        self.password = password
        self.site = site
        self.user_id = None

    def set_user_id(self, id):
        self.user_id = id