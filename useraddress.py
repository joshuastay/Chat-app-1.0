from tkinter import *


class PromptUser:
    def __init__(self, master):
        self.master = master
        self.host_add = ""
        self.port_add = ""
        self.new_user = ""
        master.title('Chat Room Login')
        master.geometry('300x150')
        master.resizable(False, False)
        self.host_entry = Entry(master, width=30)
        self.host_entry.place(x=90, y=20)
        self.host_entry.insert(0, '')
        self.port_entry = Entry(master, width=30)
        self.port_entry.place(x=90, y=50)
        self.port_entry.insert(0, '9999')
        self.user_entry = Entry(master, width=30)
        self.user_entry.place(x=90, y=80)
        self.user_entry.insert(0, 'New User')
        self.conn_butt = Button(master, text='Connect', width=10, command=self.connection)
        self.conn_butt.place(x=105, y=115)
        self.host_label = Label(master, text='Host: ')
        self.host_label.place(x=30, y=19)
        self.port_label = Label(master, text='Port: ')
        self.port_label.place(x=30, y=49)
        self.user_label = Label(master, text='Username: ')
        self.user_label.place(x=20, y=79)

    def connection(self):
        self.host_add = self.host_entry.get()
        self.port_add = self.port_entry.get()
        self.new_user = self.user_entry.get()
        self.master.destroy()

    def get_info(self):
        new_host = self.host_add
        new_port = self.port_add
        user_var = self.new_user
        return new_host, new_port, user_var
