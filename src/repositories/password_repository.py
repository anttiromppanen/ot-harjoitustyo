from entities.password import Password


class PasswordRepository:
    def __init__(self, conn):
        self._conn = conn

    def tuple_to_password(self, password):
        if not password:
            return None

        password_to_return = Password(password[1], password[2], password[3])
        password_to_return.set_user_id(password[4])

        return password_to_return

    def get_all_passwords_by_user(self, user):
        cursor = self._conn.cursor()
        cursor.execute('SELECT * FROM passwords WHERE user_id = ?', (user.user_id,))
        passwords = cursor.fetchall()
        passwords = map(self.tuple_to_password, passwords)

        return passwords