from tkinter import Tk, ttk, constants

class UserView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        add_password_button = ttk.Button(
            master=self._frame,
            text="Add password"
        )
        logout_button = ttk.Button(
            master=self._frame,
            text="Logout"
        )
        data_label = ttk.Label(master=self._frame, text="Saved passwords", font=(None, 20))

        add_password_button.grid(row=0, column=0, sticky=constants.W, padx=5, pady=5)
        logout_button.grid(row=0, column=1, sticky=constants.E, padx=5, pady=5)
        data_label.grid(row=1, column=0)

        self._frame.columnconfigure(0, weight=1, minsize=400)