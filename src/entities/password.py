class Password:
    def __init__(self, username, password, site, user_id = None):
        self.username = username
        self.password = password
        self.site = site
        self.user_id = user_id

    def set_user_id(self, id):
        self.user_id = id