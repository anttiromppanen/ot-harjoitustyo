from ui.login_view import LoginView
from ui.user_view import UserView
from ui.register_view import RegisterView
from ui.add_password_view import AddPasswordView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def handle_login_view(self):
        self._show_login_view()

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self.handle_user_view,
            self.handle_register_view,
            self.handle_login_view
        )
        self._current_view.pack()

    def handle_user_view(self, user):
        self._show_user_view(user)

    def _show_user_view(self, user):
        self._hide_current_view()
        self._current_view = UserView(self._root, user, self.handle_login_view, self.handle_add_password_view)
        self._current_view.pack()

    def handle_register_view(self):
        self._show_register_view()

    def _show_register_view(self):
        self._hide_current_view()
        self._current_view = RegisterView(self._root, self.handle_login_view)
        self._current_view.pack()

    def handle_add_password_view(self, user):
        self._show_add_password_view(user)

    def _show_add_password_view(self, user):
        self._hide_current_view()
        self._current_view = AddPasswordView(self._root, self.handle_user_view, user)
        self._current_view.pack()