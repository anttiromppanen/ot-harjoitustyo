from entities.password import Password


class PasswordRepository:
    """Salasanojen tietokantakutsuista vastaava luokka """
    def __init__(self, conn):
        """Konstruktori, luo uuden salasanojen tietokantakutsuista vastaavan olion

        Args:
            conn: db_connection luokan metodi database_connection tai test_database_connection
        """
        self._conn = conn

    def tuple_to_password(self, password):
        """Apufunktio, joka muuttaa tuple-syötteen Password-olioksi

        Args:
            password: Tuple, joka sisältää halutun Password-olion kentät
        Returns:
            Password-olio, joka muodostetaan parametristä password
        """
        if not password:
            return None

        password_to_return = Password(password[1], password[2], password[3])
        password_to_return.set_user_id(password[4])

        return password_to_return

    def get_all_passwords_by_user(self, user):
        """Palauttaa halutun käyttäjän lisäämät salasanat

        Args:
            user: User-olio, jonka lisäämät salasanat haetaan

        Returns:
            Palauttaa halutun käyttäjän lisäämät salasanat listamuodossa
        """
        cursor = self._conn.cursor()
        cursor.execute('SELECT * FROM passwords WHERE user_id = ?', (user.user_id,))
        passwords = cursor.fetchall()
        passwords = map(self.tuple_to_password, passwords)

        return list(passwords)


    def get_all_passwords(self):
        """Palauttaa kaikki järjestelmään lisätyt salasanat

        Returns:
            Palauttaa kaikki järjestelmään lisätyt salasanat listamuodossa
        """
        cursor = self._conn.cursor()
        cursor.execute('SELECT * FROM passwords')
        passwords = cursor.fetchall()
        passwords = map(self.tuple_to_password, passwords)

        return list(passwords)

    def create_password(self, password):
        """Lisää järjestelmään halutun salasanan

        Args:
            password: Password-olio, joka halutaan lisätä järjestelmään

        Returns:
            Palauttaa luodun Password-olion
        """
        cursor = self._conn.cursor()

        username = password.username
        site_password = password.password
        site = password.site
        user_id = password.user_id

        cursor.execute('''INSERT INTO passwords (username, password, site, user_id)
                        VALUES (?, ?, ?, ?)''', (username, site_password, site, user_id))

        self._conn.commit()
        return password

    def delete_all_passwords(self):
        """POISTAA KAIKKI JÄRJESTELMÄÄN LISÄTYT SALASANAT"""
        cursor = self._conn.cursor()
        cursor.execute('DELETE FROM passwords')
        self._conn.commit()