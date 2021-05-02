from db_connection import database_connection
from repositories.password_repository import (
    PasswordRepository as default_password_repository
)

class PasswordService:
    def __init__(self, password_repository = default_password_repository(database_connection())):
        self._password_repository = password_repository

    def get_passwords_by_user(self, user):
        passwords = self._password_repository.get_all_passwords_by_user(user)

        return passwords

    def add_new_password(self, password):
        added_password = self._password_repository.create_password(password)

        return added_password