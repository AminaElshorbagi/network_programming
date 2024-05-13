from socket import *
from threading import Thread


def send_message(s):
    while True :
        x= input("\nClient:")
        s.send(x.encode("utf-8"))

def recive_message(s):
    while True:
        msg = s.recv(1024)
        print("\nServer:", msg.decode("utf-8"))



sock = socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=12345
sock.connect((host,port))

t2 = Thread(target=recive_message, args=(sock,))
t1=Thread(target=send_message,args=(sock,))

t2.start()
t1.start()
