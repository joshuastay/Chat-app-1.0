import socket
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
sock.connect_ex((HOST, PORT))


frame = tk.Tk()
client_frame = clientside.ClientFrame(frame, sock, username)
frame.mainloop()
