import tkinter as tk
import tkinter.simpledialog
from tkinter.filedialog import asksaveasfile
from tkinter import ttk

from Crypto.PublicKey import RSA

import crypto_objects as co

import pickle

class EnvelopeTab(tk.Frame):

    def __init__(self, master):
        self.master = master
        super().__init__(self.master)

        # Action name label
        self.textLabel = None

        self.create_widgets()

    def create_widgets(self):
        self.textLabel = tk.Label(self, text="Digital Envelope Created Here")
        self.textLabel.pack()


class SignatureTab(tk.Frame):

    def __init__(self, master):
        self.master = master
        super().__init__(self.master)

        # Action name label
        self.textLabel = None

        self.create_widgets()

    def create_widgets(self):
        self.textLabel = tk.Label(self, text="Digital Signature Created Here")
        self.textLabel.pack()


class StampTab(tk.Frame):

    def __init__(self, master):
        self.master = master
        super().__init__(self.master)

        # Action name label
        self.textLabel = None

        self.create_widgets()

    def create_widgets(self):
        self.textLabel = tk.Label(self, text="Signed Digital Envelope Created Here")
        self.textLabel.pack()


class CryptoApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.title("NOS - 2. lab")
        self.geometry("800x600")

    def create_widgets(self):
        menubar = tk.Menu(self, tearoff=False)
        self.config(menu=menubar)

        menu_keys = tk.Menu(self, tearoff=False)

        menu_keys.add_command(label='Select New Private Key', command=self.select_private)
        menu_keys.add_command(label='Select New Public Key', command=self.select_public)
        menu_keys.add_command(label='Generate Keys', command=self.generate_keypair)

        menubar.add_cascade(menu=menu_keys, label='My Keys')

        self.create_tabs()

    def select_private(self):
        print("showing keys")

    def select_public(self):
        print("editing keys")

    def generate_keypair(self):
        """
        Definitely needs refactoring.
        Generates RSA keys and dumps them into a file

        :return: None
        """

        key_size = None

        while key_size is None or key_size < 1024 or key_size % 256 is not 0:
            key_size = tk.simpledialog.askinteger(
                "RSA key size",
                "Size must be greater than 1024 and be a multiple of 256",
                minvalue=1024)

            if key_size is None:
                return

        key = RSA.generate(key_size)

        private_key = co.RSAPrivateKey.from_crypto_key(key_size, key)
        public_key = co.RSAPublicKey.from_crypto_key(key_size, key)

        file = asksaveasfile(
            mode='wb',
            title="Save Private Key As",
            filetypes=[('Private Key (.pri)', '*.pri'), ('All Files', '*.*')],
            initialfile='private_key.pri',
            initialdir='./')

        if file is None:
            return

        pickle.dump(private_key, file)
        file.close()

        file = asksaveasfile(
            mode='wb',
            title="Save Public Key As",
            filetypes=[('Public Key (.pub)', '*.pub'), ('All Files', '*.*')],
            initialfile='public_key.pub',
            initialdir='./')

        if file is None:
            return

        pickle.dump(public_key, file)
        file.close()

    def create_tabs(self):
        action_tabs = ttk.Notebook(self)
        action_tabs.add(EnvelopeTab(action_tabs), text="Digital Envelope")
        action_tabs.add(SignatureTab(action_tabs), text="Digital Signature")
        action_tabs.add(StampTab(action_tabs), text="Signed Envelope")
        action_tabs.pack(expand=1, fill="both")


if __name__ == '__main__':
    app = CryptoApp()
    app.mainloop()