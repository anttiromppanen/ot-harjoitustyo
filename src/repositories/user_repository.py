from entities.user import User


class UserRepository:
    def __init__(self, conn):
        self._conn = conn

    def tuple_to_user(self, user):
        if not user:
            return None

        user_to_return = User(user[1], user[2])
        user_to_return.set_user_id(user[0])

        return user_to_return

    def login_user(self, user):
        cursor = self._conn.cursor()
        cursor.execute(
            'SELECT * FROM users WHERE username = ? AND password = ?',
            (user.username, user.password)
        )

        user = cursor.fetchone()
        user_to_return = self.tuple_to_user(user)

        return user_to_return

    def get_all_users(self):
        cursor = self._conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        users = map(self.tuple_to_user, users)

        return list(users)

    def create_user(self, user):
        cursor = self._conn.cursor()
        username = user.username.lower()

        cursor.execute('INSERT INTO users (username, password) values (?, ?)',
                       (username, user.password))

        self._conn.commit()

        return user

    def get_single_user(self, user):
        cursor = self._conn.cursor()

        if not user.username or not user.password: return None

        username = user.username.lower()

        cursor.execute('SELECT * FROM users WHERE username = (?)', (username,))
        result = cursor.fetchone()

        return self.tuple_to_user(result)

    def delete_all(self):
        cursor = self._conn.cursor()
        cursor.execute('DELETE FROM users')
        self._conn.commit()
