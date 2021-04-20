from tkinter import Tk, ttk, constants

class RegisterView:
    def __init__(self, root, handle_login_view):
        self._root = root
        self._frame = None
        self._initialize()
        self._handle_login_view = handle_login_view

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_register(self, username, password):
        pass

    def _handle_cancel(self):
        self._handle_login_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Register", font=(None, 20)
        )
        username_label = ttk.Label(
            master=self._frame, text="username", font=(None, 10)
        )
        username_entry = ttk.Entry(
            master=self._frame
        )
        password_label = ttk.Label(
            master=self._frame, text="password", font=(None, 10)
        )
        password_entry = ttk.Entry(
            master=self._frame, show="*"
        )
        # Add user to database and return to login screen
        register_button = ttk.Button(
            master=self._frame,
            text="Register",
            command=lambda: self._handle_register(
                username_entry.get(), password_entry.get()
            )
        )
        # Return to login screen
        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=lambda: self._handle_cancel()
        )

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=2, pady=2, ipady=5)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=2, pady=2, ipady=5)
        register_button.grid(row=3, column=0, sticky=constants.E,
            padx=2, pady=5, ipady=5)
        cancel_button.grid(row=3, column=1, sticky=constants.W,
            padx=2, pady=5, ipady=5)