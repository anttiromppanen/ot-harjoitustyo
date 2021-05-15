import unittest
from entities.password import Password
from services.password_service import PasswordService
from repositories.password_repository import PasswordRepository
from entities.user import User
from services.user_service import UserService
from repositories.user_repository import UserRepository
from db_connection import test_database_connection


class TestPasswordService(unittest.TestCase):
    def setUp(self):
        self.password_repository = PasswordRepository(test_database_connection())
        self.password_service = PasswordService(self.password_repository)
        self.password_repository.delete_all_passwords()

        self.user_repository = UserRepository(test_database_connection())
        self.user_service = UserService(self.user_repository)

        self.test_user_one = User("test_user_one", "test_pw1")
        self.test_user_two = User("test_user_two", "test_pw2")
        self.user_service.create_user(self.test_user_one)
        self.user_service.create_user(self.test_user_two)

    def test_num_of_users_correct(self):
        users = self.user_repository.get_all_users()

        self.assertEqual(len(users), 2)

    def test_add_new_password(self):
        user_for_password = self.user_repository.get_single_user(self.test_user_one)
        password_to_add = Password(
            "test_username",
            "test_pw",
            "test_site",
            user_for_password.user_id
        )
        added_password = self.password_service.add_new_password(password_to_add)

        self.assertEqual(added_password.user_id, user_for_password.user_id)
        self.assertEqual(added_password, password_to_add)

    def test_get_passwords_by_user(self):
        user_for_password = self.user_repository.get_single_user(self.test_user_one)

        for i in range(5):
            password_to_add = Password(
                f"test_username{i}",
                f"test_pw{i}",
                f"test_site{i}",
                user_for_password.user_id
            )
            self.password_service.add_new_password(password_to_add)

        passwords_by_user = self.password_service.get_passwords_by_user(user_for_password)

        self.assertEqual(len(passwords_by_user), 5)
        self.assertEqual(passwords_by_user[0].username, "test_username0")
