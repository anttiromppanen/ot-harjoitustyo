from db_connection import database_connection
from entities.user import User
from repositories.user_repository import (
    UserRepository as default_user_repository
)

class UserService:
    def __init__(self, user_repository = default_user_repository(database_connection())):

        self.user = None
        self._user_repository = user_repository

    def login_user(self, user):
        # if user exists: returns user, othwerise returns None
        self.user = self._user_repository.login_user(user)

        return self.user

    def get_user(self, user):
        user_by_username = self._user_repository.get_single_user(user)

        return user_by_username

    def create_user(self, user):
        # username must be unique
        # returns None if username already exists
        # otherwise adds new user and returns it
        if self.get_user(user):
            return None

        new_user = self._user_repository.create_user(user)

        return new_user