from tkinter import Tk, ttk, constants, messagebox
from services.password_service import PasswordService
from entities.password import Password

class AddPasswordView:
    def __init__(self, root, handle_user_view, user=None):
        self._root = root
        self._frame = None
        self.user = user
        self._handle_user_view = handle_user_view
        self._password_service = PasswordService()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def handle_back_to_user_view(self):
        self._handle_user_view(self.user)

    def handle_add_new_password(self, site, username, password):
        if not site or not username or not password:
            return messagebox.showerror('Error', 'No empty fields allowed')

        user_id = self.user.user_id
        new_password = Password(username, password, site, user_id)
        result = self._password_service.add_new_password(new_password)

        messagebox.showinfo('Info', 'Password added')

        # Reset fields
        self.site_entry.delete(0, "end")
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        
        return result

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Add new credentials", font=(None, 20)
        )
        site_label = ttk.Label(
            master=self._frame, text="site", font=(None, 10)
        )
        self.site_entry = ttk.Entry(
            master=self._frame
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
        submit_button = ttk.Button(
            master=self._frame,
            text="Submit",
            command=lambda: self.handle_add_new_password(
                self.site_entry.get(),
                self.username_entry.get(),
                self.password_entry.get()
            )
        )
        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=lambda: self.handle_back_to_user_view()
        )

        heading_label.grid(row=0, column=0, columnspan=2,
            sticky=constants.W, padx=5, pady=5)

        site_label.grid(row=1, column=0)
        self.site_entry.grid(
            row=1,
            column=1,
            sticky=(constants.E, constants.W),
            padx=2,
            pady=2,
            ipady=5
        )

        username_label.grid(row=2, column=0)
        self.username_entry.grid(
            row=2,
            column=1,
            sticky=(constants.E, constants.W),
            padx=2,
            pady=2,
            ipady=5
        )

        password_label.grid(row=3, column=0)
        self.password_entry.grid(
            row=3,
            column=1,
            sticky=(constants.E, constants.W),
            padx=2,
            pady=2,
            ipady=5
        )

        submit_button.grid(
            row=4,
            column=0,
            sticky=constants.E,
            padx=2,
            pady=5,
            ipady=5
        )
        cancel_button.grid(
            row=4,
            column=1,
            sticky=constants.W,
            padx=2,
            pady=5,
            ipady=5
        )