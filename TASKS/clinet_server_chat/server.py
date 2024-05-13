from socket import *
from threading import Thread


def send_message(s):
    while True :
        s.send(input("\nServer:").encode("utf-8"))

def recive_message(s):
    while True:
        msg = s.recv(1024)
        print("\nClient:", msg.decode("utf-8"))


sock = socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=12345
sock.bind((host,port))
sock.listen(5)


while True:
    client_socket , client_address = sock.accept()
    print("Get connection from ", client_address)
    t1=Thread(target=send_message,args=(client_socket,))
    t2=Thread(target=recive_message,args=(client_socket,))
    t1.start()
    t2.start()