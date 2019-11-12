import socket
import threading
def read_sok():
     while True:
         data = sor.recv(1024)
         print(data.decode('utf-8'))

server = '192.168.88.89', 5050
alias = input("Введiть псевдонiм: ")
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('127.0.0.1', 0))
sor.sendto((alias+' Connect to server').encode('utf-8'), server)
potok = threading.Thread(target=read_sok)
potok.start()
while 1 :
    mensahe = input('message: ')
    sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)
