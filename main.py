import tkinter as tk
from tkinter import ttk


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

        # Main tab control
        self.actionTabs = None

        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.title("NOS - 2. lab")
        self.geometry("800x600")

    def create_widgets(self):
        self.create_tabs()

    def create_tabs(self):
        self.actionTabs = ttk.Notebook(self)
        self.actionTabs.add(EnvelopeTab(self.actionTabs), text="Digital Envelope")
        self.actionTabs.add(SignatureTab(self.actionTabs), text="Digital Signature")
        self.actionTabs.add(StampTab(self.actionTabs), text="Signed Envelope")
        self.actionTabs.pack(expand=1, fill="both")


if __name__ == '__main__':
    app = CryptoApp()
    app.mainloop()