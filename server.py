import socket
import tkinter as tk
import threading
from _thread import start_new_thread

chat_window = tk.Tk()

hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

conn_list = list()


def client_scan():
    global conn
    while True:
        conn, addr = sock.accept()
        start_new_thread(chat_in, (conn, addr))
        conn_list.append(conn)


def chat_in(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            conn_list.remove(conn)
            break
        for each in conn_list:
            each.sendall(data)
        if data:
            host_chat.config(state=tk.NORMAL)
            host_chat.insert(tk.INSERT, data.decode() + '\n')
            host_chat.config(state=tk.DISABLED)
        else:
            host_chat.config(state=tk.DISABLED)


def chat_out(event=None):
    global conn_list, conn
    message = '<Host>: ' + host_field.get()
    host_chat.config(state=tk.NORMAL)
    host_chat.insert(tk.INSERT, message + '\n')
    host_chat.config(state=tk.DISABLED)
    for each in conn_list:
        each.sendall(message.encode())
    host_chat.insert(tk.INSERT, message)
    host_field.delete(0, tk.END)


send_button = tk.Button(chat_window, text='Send', command=chat_out)
send_button.place(x=440, y=319, width=50)
host_field = tk.Entry(chat_window, width=50)
host_field.place(x=15, y=320, width=415, height=24)
host_field.bind('<Return>', chat_out)
get_clients = threading.Thread(target=client_scan)
get_clients.daemon = True
get_clients.start()

host_chat = tk.Text(chat_window, height=19, width=50)
host_chat.insert(tk.INSERT, 'Server started at: ' + HOST + ':' + str(PORT) + '\n')
host_chat.pack(pady=5, padx=5, fill='x')
chat_window.geometry('500x350')
chat_window.config(bg='black')
chat_window.resizable(False, False)
chat_window.title('Chat Room Host')
chat_window.mainloop()
