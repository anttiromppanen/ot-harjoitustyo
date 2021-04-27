import tkinter as tk
from tkinter import ttk, constants
from services.password_service import PasswordService

class UserView:
    def __init__(self, root, user, handle_login_view):
        self._root = root
        self._frame = None
        self.user = user
        self._password_service = PasswordService()
        self._handle_login_view = handle_login_view
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def handle_logout(self):
        self._handle_login_view()

    def insert_to_tree(self):
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
        self._frame = ttk.Frame(master=self._root)
        style = ttk.Style()

        style.configure('Treeview', rowheight=40)

        add_password_button = ttk.Button(
            master=self._frame,
            text="Add password"
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