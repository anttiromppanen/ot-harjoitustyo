import unittest
from entities.password import Password
from entities.user import User
from repositories.password_repository import PasswordRepository
from repositories.user_repository import UserRepository
from db_connection import test_database_connection

class TestPasswordRepository(unittest.TestCase):
    def setUp(self):
        # Reset tables users, passwords
        self.password_repository = PasswordRepository(test_database_connection())
        self.user_repository = UserRepository(test_database_connection())
        self.password_repository.delete_all_passwords()
        self.user_repository.delete_all()

        self.test_user_one = User('testiuser', 'testiuser666', 1)
        self.test_user_two = User('secondtestuesr', 'testingggggg', 2)
        self.test_user_one = self.user_repository.create_user(self.test_user_one)
        self.test_user_two = self.user_repository.create_user(self.test_user_two)
        
        self.test_password_one = Password('matti', 'teppo', 'www.vauva.fi')
        self.test_password_two = Password('testpassword', 'testpassword2', 'www.coinbase.com')
        self.test_password_one.set_user_id(self.test_user_one.user_id)
        self.test_password_two.set_user_id(self.test_user_one.user_id)

    def test_create_password(self):
        self.password_repository.create_password(self.test_password_one)
        passwords = self.password_repository.get_all_passwords()

        self.assertEqual(len(passwords), 1)
        self.assertEqual(passwords[0].username, self.test_password_one.username)

    def test_get_all_users(self):
        user_id = self.test_user_one.user_id

        for i in range(5):
            password = Password(
                f'user{i}',
                f'password{i}',
                f'site{i}',
                user_id
            )
            self.password_repository.create_password(password)

        passwords = self.password_repository.get_all_passwords()

        self.assertEqual(len(passwords), 5)
        self.assertEqual(passwords[2].username, 'user2')

    def test_get_all_passwords_by_user(self):
        user_id = self.test_user_one.user_id

        for i in range(5):
            password = Password(
                f'user{i}',
                f'password{i}',
                f'site{i}',
                user_id
            )
            self.password_repository.create_password(password)

        user_id = self.test_user_two.user_id

        for i in range(5, 10):
            password = Password(
                f'user{i}',
                f'password{i}',
                f'site{i}',
                user_id
            )
            self.password_repository.create_password(password)

        passwords_by_user_one = self.password_repository.get_all_passwords_by_user(self.test_user_one)

        self.assertEqual(len(passwords_by_user_one), 5)
        self.assertEqual(passwords_by_user_one[1].user_id, self.test_user_one.user_id)

    def test_tuple_to_password_returns_none_if_no_password_given(self):
        result = self.password_repository.tuple_to_password(None)

        self.assertIsNone(result)