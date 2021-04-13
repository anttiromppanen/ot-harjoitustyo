from tkinter import Tk, ttk, constants
from db_connection import database_connection
from repositories.user_repository import UserRepository
from ui.user_view import UserView
from entities.user import User


class LoginView:
    def __init__(self, root, handle_user_view):
        self._root = root
        self._frame = None
        self._initialize()
        self._user = None
        self._handle_user_view = handle_user_view

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_login(self, username, password):
        user_repository = UserRepository(database_connection())
        self._user = user_repository.login_user(User(username, password))

        # if valid username and password, move into user view
        # else reset password field and print error
        if self._user:
            self._handle_user_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(
            master=self._frame, text="Welcome, please log in or register", font=(None, 20))
        username_label = ttk.Label(
            master=self._frame, text="username", font=(None, 10))
        username_entry = ttk.Entry(master=self._frame)
        password_label = ttk.Label(
            master=self._frame, text="password", font=(None, 10))
        password_entry = ttk.Entry(master=self._frame, show="*")
        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=lambda: self._handle_login(
                username_entry.get(), password_entry.get())
        )
        register_button = ttk.Button(master=self._frame, text="Register")

        # grey out register button until working
        style_ref = ttk.Style()
        style_ref.configure("style_name.TLabel", foreground='grey')
        register_button['style'] = "style_name.TLabel"

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=2, pady=2, ipady=5)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=2, pady=2, ipady=5)
        login_button.grid(row=3, column=0, sticky=constants.E,
                          padx=2, pady=5, ipady=5)
        register_button.grid(
            row=3, column=1, sticky=constants.W, padx=2, pady=5, ipady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)
