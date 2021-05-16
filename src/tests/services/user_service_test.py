import unittest
from entities.user import User
from services.user_service import UserService
from repositories.user_repository import UserRepository
from db_connection import test_database_connection


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository(test_database_connection())
        self.user_service = UserService(self.user_repository)
        self.user_repository.delete_all()

        self.test_user_one = User('testuser', 'testuser1', 1)
        self.test_user_two = User('secondo', 'testuser2', 2)


    def test_create_user(self):
        result = self.user_service.create_user(self.test_user_one)
        users = self.user_repository.get_all_users()

        self.assertEqual(result.username, self.test_user_one.username)
        self.assertEqual(len(users), 1)

    def test_create_user_fails_if_too_long_username(self):
        test_user = User('a' * 31, 'test_pw')
        result = self.user_service.create_user(test_user)
        users = self.user_repository.get_all_users()

        self.assertEqual(result, None)
        self.assertEqual(len(users), 0)

    def test_create_user_fails_if_too_long_password(self):
        test_user = User('aasi_boy', 'a' * 51)
        result = self.user_service.create_user(test_user)
        users = self.user_repository.get_all_users()

        self.assertEqual(result, None)
        self.assertEqual(len(users), 0)

    def test_create_user_returns_none_if_user_exists(self):
        user = self.user_service.create_user(self.test_user_one)
        result = self.user_service.create_user(self.test_user_one)

        self.assertIsNone(result)

    def test_create_user_returns_none_if_no_username_given(self):
        test_user = User(None, 'testing', 69)
        result = self.user_service.create_user(test_user)

        self.assertIsNone(result)

    def test_create_user_returns_none_if_no_password_given(self):
        test_user = User('testing', None, 69)
        result = self.user_service.create_user(test_user)

        self.assertIsNone(result)

    def test_get_user(self):
        self.user_service.create_user(self.test_user_two)
        result = self.user_service.get_user(self.test_user_two)

        self.assertEqual(result.username, self.test_user_two.username)

    def test_login_user(self):
        self.user_service.create_user(self.test_user_one)
        result = self.user_service.login_user(self.test_user_one)

        self.assertEqual(result.username, self.test_user_one.username)