from socket import *
import  threading
from tkinter import *

sessions=[]

s=socket(AF_INET,SOCK_STREAM)
s.bind(('127.0.0.1',4000))
s.listen(50)


window=Tk()
window.title("chat server")
window.geometry("400x400")


label=Label(window)
label.grid(row=3,column=3)


entry=Entry(window,width="40")
entry.grid(row=1, column=30)


def clicked():
    message = entry.get()
    for session in sessions:
        session.send(("server:"+ message).encode('utf-8'))
    entry.delete(0,END)


btn = Button(window,text="send" ,bg= "green",fg="white",width=8,height=1,command=clicked)
btn.grid(row=1,column=4)

def recv_thread(c,ad):
    while True:
        message=c.recv(1024).decode('utf-8')
        label['text']=str(ad[1])+":"+message
        for session in sessions:
            if (session!=c):
                session.send((str(ad[1])+":"+message).encode('utf-8'))


def main_thread(s):
    while True:
        c,ad=s.accept()
        sessions.append(c)
        label['text']="new connection from "+str(ad[1])
        threading.Thread(target=recv_thread,args=(c,ad)).start()


threading.Thread(target=main_thread,args=(s,)).start()
window.mainloop()

