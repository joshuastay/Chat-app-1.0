import socket
import threading
import tkinter as tk
import useraddress
import clientside

prompt = tk.Tk()
prompt_user = useraddress.PromptUser(prompt)
prompt.mainloop()
HOST = prompt_user.get_info()[0]
PORT = int(prompt_user.get_info()[1])
username = prompt_user.get_info()[2]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
frame = tk.Tk()
client_frame = clientside.ClientFrame(frame)
sock.connect((HOST, PORT))


def chat_in():
    while True:
        data = sock.recv(1024)
        client_frame.message_recv(data)


def chat_out(event):
    message = '<' + username + '>: ' + entry.get()
    sock.send(message.encode())
    entry.delete(0, tk.END)


thread1 = threading.Thread(target=chat_in)
thread1.daemon = True
thread1.start()
entry = tk.Entry(frame, width='50')
entry.place(x=15, y=320, width=415, height=24)
entry.bind('<Return>', chat_out)
button = tk.Button(frame, text='Send', command=chat_out)
button.place(x=440, y=319, width=50)
frame.mainloop()
