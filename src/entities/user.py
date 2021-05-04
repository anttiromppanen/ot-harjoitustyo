class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää

    Attributes:
        username: String, käyttäjänimi
        password: String, Salasana
        user_id: int, käyttäjän uniikki id
    """
    def __init__(self, username, password, user_id = None):
        """Konstruktori, luo uuden käyttäjän

        Args:
            username: Käyttäjänimi, pakollinen
            password: Salasana, pakollinen
            user_id: Käyttäjän id, oletusarvo None
        """
        self.username = username
        self.password = password
        self.user_id = user_id

    def set_user_id(self, id):
        """Mahdollistaa user_id:n asettamisen käyttäjän alustamisen jälkeen

        Args:
            id: Käyttäjälle asetettava user_id
        """
        self.user_id = id
