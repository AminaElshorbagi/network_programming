from socket import *
import threading
from tkinter import *


sock = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 4000
sock.connect((host,port))

window = Tk()
window.title("chat client")
window.geometry("400x400")

label = Label(window)
label.grid(row=3,column=3)

entry = Entry(window,width="40")
entry.grid(row=1,column=30)


def clicked():
    message = entry.get()
    sock.send(message.encode('utf-8'))
    entry.delete(0,END)


btn = Button(window,text="send" ,bg= "green",fg="white",width=8,height=1,command=clicked)
btn.grid(row=1,column=4)


def recv_thread(s):
    while True:
        label['text'] = s.recv(1024).decode('utf-8')


threading.Thread(target=recv_thread,args=(sock,)).start()


window.mainloop()
















