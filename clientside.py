from tkinter import *


class ClientFrame:
    def __init__(self, master):
        self.master = master
        master.title("Chat Room")
        master.geometry('500x350')
        master.config(bg='black')
        master.resizable(False, False)
        self.message_board = Text(master, height=19, width=50)
        self.message_board.pack(pady=5, padx=5, fill='x')

    def message_recv(self, message):
        if message:
            self.message_board.config(state=NORMAL)
            self.message_board.insert(INSERT, message.decode() + '\n')
            self.message_board.config(state=DISABLED)
        else:
            self.message_board.config(state=DISABLED)
