import tkinter as tk
from tkinter import ttk, constants
from services.password_service import PasswordService

class UserView:
    def __init__(self, root, user, handle_login_view, handle_add_password_view):
        """Käyttäjänäkymästä vastaava käyttöliittymäluokka

        Args:
            root: Juurielementti, joka hallitsee nykyistä näkymää
            user: User-luokan olio
            handle_login_view: UI-luokan metodi, joka siirtää näkymän LoginViewiin
            handle_add_password_view: UI-luokan metodi, joka siirtää näkymän AddPasswordViewiin
        """
        self._root = root
        self._frame = None
        self.user = user
        self._password_service = PasswordService()
        self._handle_login_view = handle_login_view
        self._handle_add_password_view = handle_add_password_view
        self._initialize()

    def pack(self):
        """Pakkaa käyttöliittymän komponentit ennen renderöintiä"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa tämänhetkisen näkymän"""
        self._frame.destroy()

    def handle_logout(self):
        """Kirjaa käyttäjän ulos järjestelmästä"""
        message_box = tk.messagebox.askquestion('Info', f'Log out user {self.user.username}?')

        if message_box == 'yes':
            self._handle_login_view()
        else:
            return

    def handle_move_to_add_view(self, user):
        """Siirtää näkymän AddPasswordViewiin kun nappia painetaan"""
        self._handle_add_password_view(user)

    def insert_to_tree(self):
        """Luo näkymän käyttäjien lisäämille salasanoille"""
        passwords = self._password_service.get_passwords_by_user(self.user)

        self.numOfPasswords = 1
        self.iid = 0

        for x in passwords:
            self.tree.insert(
                '',
                'end',
                iid=self.iid,
                text=self.numOfPasswords,
                values=(x.site, x.username, x.password)
            )

            self.iid = self.iid + 1
            self.numOfPasswords = self.numOfPasswords + 1

    def _initialize(self):
        """Initialisoi näkymän"""
        self._frame = ttk.Frame(master=self._root)
        style = ttk.Style()

        style.configure('Treeview', rowheight=40)

        add_password_button = ttk.Button(
            master=self._frame,
            text="Add password",
            command=lambda: self._handle_add_password_view(self.user)
        )
        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=lambda: self.handle_logout()
        )
        data_label = ttk.Label(master=self._frame, text="Saved passwords", font=(None, 20))

        add_password_button.grid(row=0, column=0, sticky=constants.W, padx=5, pady=5)
        logout_button.grid(row=0, column=1, sticky=constants.E, padx=5, pady=5)
        data_label.grid(row=1, column=0, sticky=(constants.E, constants.W), pady=20)

        self.tree = ttk.Treeview(self._frame, columns=('Site', 'Username', 'Password'))
        self.tree.heading('#0', text='#')
        self.tree.heading('#1', text='Site')
        self.tree.heading('#2', text='Username')
        self.tree.heading('#3', text="Password")

        self.tree.column('#0', width=30)

        self.tree.grid(row=2, columnspan=4, sticky='nsew')

        self._frame.columnconfigure(0, weight=1, minsize=400)

        self.insert_to_tree()