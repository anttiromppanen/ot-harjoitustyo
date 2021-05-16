from tkinter import Tk, ttk, constants, messagebox
from db_connection import database_connection
from ui.user_view import UserView
from entities.user import User
from services.user_service import UserService

class LoginView:
    def __init__(self, root, handle_user_view, handle_register_view, handle_login_view):
        """Kirjautumisnäkymästä vastaava käyttöliittymäluokka
        
        Args:
            root: Juurielementti, joka hallitsee nykyistä näkymää
            handle_user_view: UI-luokan metodi, joka siirtää näkymän UserViewiin
            handle_register_view: UI-luokan metodi, joka siirtää näkymän RegisterViewiin
            handle_login_view: UI-luokan metodi, joka siirtää näkymän LoginViewiin
        """
        self._root = root
        self._frame = None
        self._initialize()
        self.user = None
        self._user_service = UserService()
        self._handle_user_view = handle_user_view
        self._handle_register_view = handle_register_view
        self._handle_login_view = handle_login_view

    def pack(self):
        """Pakkaa käyttöliittymän komponentit ennen renderöintiä"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa tämänhetkisen näkymän"""
        self._frame.destroy()

    def _handle_login(self, username, password):
        """Kirjaa käyttäjän järjestelmään, heittää virheen virheellisillä syötteillä
        
        Args:
            username: String
            password: String 
        """
        self.user = self._user_service.login_user(User(username, password))

        # if not valid credentials, reset password entry and show error
        # else log user in
        if not username or not password:
            return messagebox.showerror('Error', 'No empty fields allowed')

        if not self.user:
            self.password_entry.delete(0, 'end')
            return messagebox.showerror('Error', 'Invalid username or password')

        self._handle_user_view(self.user)

    def _handle_register_button(self):
        """Siirtää näkymän RegisterViewiin kun nappia painetaan"""
        self._handle_register_view()

    def _initialize(self):
        """Initialisoi näkymän"""
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Welcome, please log in or register", font=(None, 20)
        )
        username_label = ttk.Label(
            master=self._frame, text="username", font=(None, 10)
        )
        self.username_entry = ttk.Entry(
            master=self._frame
        )
        password_label = ttk.Label(
            master=self._frame, text="password", font=(None, 10)
        )
        self.password_entry = ttk.Entry(
            master=self._frame, show="*"
        )
        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=lambda: self._handle_login(
                self.username_entry.get(), self.password_entry.get()
            )
        )
        register_button = ttk.Button(
            master=self._frame,
            text="Register",
            command=lambda: self._handle_register_button()
        )

        heading_label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky=constants.W,
            padx=5,
            pady=5
        )

        username_label.grid(row=1, column=0)
        self.username_entry.grid(
            row=1,
            column=1,
            sticky=(constants.E, constants.W),
            padx=2,
            pady=2,
            ipady=5
        )

        password_label.grid(row=2, column=0)
        self.password_entry.grid(
            row=2,
            column=1,
            sticky=(constants.E, constants.W),
            padx=2,
            pady=2,
            ipady=5
        )

        login_button.grid(
            row=3,
            column=0,
            sticky=constants.E,
            padx=2,
            pady=5,
            ipady=5
        )
        register_button.grid(
            row=3,
            column=1,
            sticky=constants.W,
            padx=2,
            pady=5,
            ipady=5
        )

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)
