import socket
import tkinter as tk
import threading
from _thread import start_new_thread

frame = tk.Tk()

HOST = '192.168.0.164'
PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
conn_list = list()
#conn, addr = sock.accept()

def client_scan():
    global conn, addr
    while True:
        conn, addr = sock.accept()
        start_new_thread(chat_in, (conn, addr))
        conn_list.append(conn)


def chat_in(conn, addr):
    global conn_list
    while True:
        data = conn.recv(1024)
        for each in conn_list:
            each.sendall(data)
        if data:
            text.config(state=tk.NORMAL)
            text.insert(tk.INSERT, data.decode() + '\n')
            text.config(state=tk.DISABLED)
        else:
            text.config(state=tk.DISABLED)


def chat_out():
    while True:
        message = input("Type Message")
        conn.sendall(message.encode())


# entry = tk.Entry(frame, width=50)
# entry.place(x=15, y=320, width=415, height=24)
# entry.bind()
get_clients = threading.Thread(target=client_scan)
get_clients.daemon = True
get_clients.start()

chat_box = threading.Thread(target=chat_in)
chat_box.daemon = True
chat_box.start()

text = tk.Text(frame, height=19, width=50)
text.pack(pady=5, padx=5, fill='x')
frame.geometry('500x350')
frame.config(bg='black')
frame.resizable(False, False)
frame.mainloop()
