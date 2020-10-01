import socket
import tkinter as tk
import useraddress
import clientside

# Prompt the user to specify where the server is running
# Retrieves Ip address, Port and Username from User
prompt = tk.Tk()
prompt_user = useraddress.PromptUser(prompt)
prompt.mainloop()

HOST = prompt_user.get_info()[0]
PORT = int(prompt_user.get_info()[1])
username = prompt_user.get_info()[2]

# Open socket using address given by user
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect_ex((HOST, PORT))

# Load main window for chatroom, closes socket after window is closed
frame = tk.Tk()
client_frame = clientside.ClientFrame(frame, sock, username)
frame.mainloop()
sock.shutdown(socket.SHUT_RDWR)
sock.close()