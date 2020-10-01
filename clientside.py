from tkinter import *
import threading


class ClientFrame:
    def __init__(self, master, sock, user):
        self.master = master
        master.title("Chat Room")
        master.geometry('500x350')
        master.config(bg='black')
        master.resizable(False, False)
        self.message_board = Text(master, height=19, width=50)
        self.message_board.pack(pady=5, padx=5, fill='x')
        self.sock = sock
        self.user = user
        self.user_message = Entry(master, width=50)
        self.user_message.place(x=15, y=320, width=415, height=24)
        self.user_message.bind('<Return>', self.chat_out)
        self.send_button = Button(master, text='Send', command=self.chat_out)
        self.send_button.place(x=440, y=319, width=50)
        room_thread = threading.Thread(target=self.chat_in)
        room_thread.daemon = True
        room_thread.start()
        self.user_in()

    def message_recv(self, message):
        if message:
            self.message_board.config(state=NORMAL)
            self.message_board.insert(INSERT, message.decode() + '\n')
            self.message_board.config(state=DISABLED)
        else:
            self.message_board.config(state=DISABLED)

    def chat_in(self):
        while True:
            try:
                data = self.sock.recv(1024)
                self.message_recv(data)
            except:
                self.message_board.insert(INSERT, 'Connection Failed!\n')
                break

    def chat_out(self, event=None):
        try:
            message = '<' + self.user + '>: ' + self.user_message.get()
            self.sock.send(message.encode())
            self.user_message.delete(0, END)
        except:
            self.message_board.insert(INSERT, 'Message Send Failed, No Connection Found!\n')
            self.user_message.delete(0, END)

    def user_in(self):
        enter_chat = 'User: <' + self.user + '> has entered the chat!'
        try:
            self.sock.send(enter_chat.encode())
        except:
            pass
