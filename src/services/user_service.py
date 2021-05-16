from db_connection import database_connection
from repositories.user_repository import (
    UserRepository as default_user_repository
)

class UserService:
    """Käyttäjien sovelluslogiikasta vastaava luokka"""
    def __init__(self, user_repository = default_user_repository(database_connection())):
        """Konstruktori, luo uuden käyttäjien sovelluslogiikasta vastaavan palvelun

        Args:
            user: Kirjautunut käyttäjä, oletusarvoltaan None
            user_repository: Vapaaehtoinen, oletusarvoltaan UserRepository-olio
        """
        self.user = None
        self._user_repository = user_repository

    def login_user(self, user):
        """Kirjaa käyttäjän järjestelmään

        Args:
            user: User-olio, jolla käyttäjä kirjataan sisään
        Returns
            Palauttaa User-olion, joka kirjataan järjestelmään
        """
        self.user = self._user_repository.login_user(user)

        return self.user

    def get_user(self, user):
        """Hakee halutun käyttäjän tietokannasta

        Args:
            user: User-olio, joka etsitään tietokannasta
        Returns:
            Palauttaa User-olion, jos käyttäjä löytyy tietokannasta
            tai None, jos käyttäjää ei löydy
        """
        user_by_username = self._user_repository.get_single_user(user)

        return user_by_username

    def create_user(self, user):
        """Luo uuden käyttäjän järjestelmään

        Args:
            user: User-olio joka lisätään järjestelmään
        Returns:
            Palauttaa lisätyn User-olion
            Jos käyttäjä löytyy jo järjestelmästä tai User-olio on puutteellinen
            palautetaan None
        """
        if self.get_user(user):
            return None
        if not user.username or not user.password:
            return None

        new_user = self._user_repository.create_user(user)

        return new_user
