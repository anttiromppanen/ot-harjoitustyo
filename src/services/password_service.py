from db_connection import database_connection
from repositories.password_repository import (
    PasswordRepository as default_password_repository
)

class PasswordService:
    """Salasanojen sovelluslogiikasta vastaava luokka"""
    def __init__(self, password_repository = default_password_repository(database_connection())):
        """Konstruktori, luo uuden salasanojen sovelluslogiikasta vastaavan palvelun

        Args:
            password_repository: Vapaaehtoinen, oletusarvoltaan PasswordRepository-olio
        """
        self._password_repository = password_repository

    def get_passwords_by_user(self, user):
        """Hakee tietyn käyttäjän järjestelmään lisäämät salasanat

        Args:
            user: User-olio, jonka lisäämät salasanat halutaan hakea
        Returns:
            Halutun käyttäjän lisäämät salasanat lista muodossa
        """
        passwords = self._password_repository.get_all_passwords_by_user(user)

        return passwords

    def add_new_password(self, password):
        """Lisää uuden salasanan järjestelmään

        Args:
            password: Password-olio, jonka käyttäjä haluaa lisätä järjestelmään
        Returns
            Palauttaa lisätyn Password-olion
        """
        added_password = self._password_repository.create_password(password)

        return added_password
