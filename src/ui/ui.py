from ui.login_view import LoginView
from ui.user_view import UserView
from ui.register_view import RegisterView
from ui.add_password_view import AddPasswordView

class UI:
    def __init__(self, root):
        """Eri käyttöliittymien hallinnasta vastaava luokka

        Args:
            root: Juurielementti, joka hallitsee nykyistä näkymää
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Suoritetaan kun sovellus käynnistetään, käyttäjälle näytetään LoginView"""
        self._show_login_view()

    def _hide_current_view(self):
        """Poistaa nykyisen näkymän näkyviltä"""
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def handle_login_view(self):
        """Siirtää näkymän LoginViewiin"""
        self._show_login_view()

    def _show_login_view(self):
        """LoginViewin näyttämisestä vastaava metodi"""
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self.handle_user_view,
            self.handle_register_view,
            self.handle_login_view
        )
        self._current_view.pack()

    def handle_user_view(self, user):
        """Siirtää näkymän UserViewiin"""
        self._show_user_view(user)

    def _show_user_view(self, user):
        """UserViewin näyttämisestä vastaava metodi"""
        self._hide_current_view()
        self._current_view = UserView(self._root, user, self.handle_login_view, self.handle_add_password_view)
        self._current_view.pack()

    def handle_register_view(self):
        """Siirtää näkymän RegisterViewiin"""
        self._show_register_view()

    def _show_register_view(self):
        """RegisterViewin näyttämisestä vastaava metodi"""
        self._hide_current_view()
        self._current_view = RegisterView(self._root, self.handle_login_view)
        self._current_view.pack()

    def handle_add_password_view(self, user):
        """Siirtää näkymän AddPasswordViewiin"""
        self._show_add_password_view(user)

    def _show_add_password_view(self, user):
        """AddPasswordViewin näyttämisestä vastaava metodi"""
        self._hide_current_view()
        self._current_view = AddPasswordView(self._root, self.handle_user_view, user)
        self._current_view.pack()