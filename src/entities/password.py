class Password:
    """Luokka, joka kuvaa yksittäistä käyttäjän lisäämää salasanaa

    Attributes:
        username: String, sivuston käyttäjänimi
        password: String, sivuston salasana
        site: String, sivusto johon käyttäjänimi sekä salasana liittyvät
        user_id: int, salasanan järjestelmään lisänneen käyttäjän id
    """
    def __init__(self, username, password, site, user_id = None):
        """Konstruktori, luo uuden salasanan

        Args:
            username: Käyttäjänimi sivustolle
            password: Salasana sivustolle
            site: Sivusto, johon käyttäjänimi sekä salasana liittyvät
            user_id: Salasanan järjestelmään lisänneen käyttäjän id
        """
        self.username = username
        self.password = password
        self.site = site
        self.user_id = user_id

    def set_user_id(self, id):
        """Mahdollistaa user_id:n asettamisen salasanan alustamisen jälkeen

        Args:
            id: Salasanalle asetettava user_id
        """
        self.user_id = id
