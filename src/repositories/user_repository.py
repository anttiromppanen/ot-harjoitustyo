from entities.user import User


class UserRepository:
    """Käyttäjien tietokantakutsuista vastaava luokka """
    def __init__(self, conn):
        """Konstruktori, luo uuden käyttäjien tietokantakutsuista vastaavan olion

        Args:
            conn: db_connection luokan metodi database_connection tai test_database_connection
        """
        self._conn = conn

    def tuple_to_user(self, user):
        """Apufunktio, joka muuttaa tuple-syötteen User-olioksi

        Args:
            user: Tuple, joka sisältää halutun User-olion kentät
        Returns:
            User-olio, joka muodostetaan parametristä user
        """
        if not user:
            return None

        user_to_return = User(user[1], user[2])
        user_to_return.set_user_id(user[0])

        return user_to_return

    def login_user(self, user):
        """Tarkastaa löytyykö parametrin käyttäjä tietokannasta

        Args:
            user: User-olio
        Returns:
            Jos paratetrin arvolla löydetään käyttäjä tietokannasta, palautetaan se User-oliona
        """
        cursor = self._conn.cursor()
        cursor.execute(
            'SELECT * FROM users WHERE username = ? AND password = ?',
            (user.username, user.password)
        )

        user = cursor.fetchone()
        user_to_return = self.tuple_to_user(user)

        return user_to_return

    def get_all_users(self):
        """Palauttaa kaikki käyttäjät tietokannasta

        Returns:
            Palauttaa kaikki käyttäjät tietokannasta listana
        """
        cursor = self._conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        users = map(self.tuple_to_user, users)

        return list(users)

    def create_user(self, user):
        """Luo tietokantaan uuden käyttäjän parametrin arvoilla

        Args:
            user: User-olio, joka lisätään järjestelmään
        Returns:
            Palauttaa luodun User-olion
        """
        cursor = self._conn.cursor()
        username = user.username.lower()

        cursor.execute('INSERT INTO users (username, password) values (?, ?)',
                       (username, user.password))

        self._conn.commit()

        return user

    def get_single_user(self, user):
        """Hakee järjestelmästä parametrinä annetun käyttäjän

        Args:
            user: User-olio
        Returns:
            Palauttaa luodun User-olion
        """
        cursor = self._conn.cursor()

        if not user.username or not user.password: return None

        username = user.username.lower()

        cursor.execute('SELECT * FROM users WHERE username = (?)', (username,))
        result = cursor.fetchone()

        return self.tuple_to_user(result)

    def delete_all(self):
        """POISTAA JÄRJESTELMÄSTÄ KAIKKI KÄYTTÄJÄT"""
        cursor = self._conn.cursor()
        cursor.execute('DELETE FROM users')
        self._conn.commit()
