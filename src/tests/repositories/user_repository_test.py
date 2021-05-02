import unittest
from entities.user import User
from repositories.user_repository import UserRepository
from db_connection import test_database_connection


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository(test_database_connection())
        self.user_repository.delete_all()

        self.test_user_one = User('test_user_one', 'testpw')
        self.test_user_two = User('test_user_two', 'test')

        self.user_repository.create_user(self.test_user_one)
        self.user_repository.create_user(self.test_user_two)

    def test_get_all_users(self):
        users = self.user_repository.get_all_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.test_user_one.username)

    def test_login_user(self):
        user = self.user_repository.login_user(self.test_user_one)

        self.assertEqual(user.username, self.test_user_one.username)

    def test_login_user_fails_with_wrong_credentials(self):
        invalid_user = User('test_user_one', 'passwordwrong')
        user = self.user_repository.login_user(invalid_user)

        self.assertEqual(user, None)

    def test_create_user(self):
        user = User('masamainio', 'anttiangeli')
        created_user = self.user_repository.create_user(user)
        users = self.user_repository.get_all_users()

        self.assertEqual(created_user.username, 'masamainio')
        self.assertEqual(len(users), 3)

    def test_get_single_user(self):
        user = self.user_repository.get_single_user(self.test_user_one)

        self.assertEqual(user.username, self.test_user_one.username)

    def test_get_single_user_returns_none_if_not_found(self):
        fake_user = User('risu', 'mies')
        user = self.user_repository.get_single_user(fake_user)

        self.assertEqual(user, None)
