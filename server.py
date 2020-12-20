import socket
import sys

host= "192.168.56.102"
port = 6789
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)

data,addr = s.recvfrom(1024)

file = open(data,'wb')

while True:
    print("Dapat capaian dari: "+str(addr))
    print("Fail diterima:",data)
    
    data,addr = s.recvfrom(1024)
    while data:
        file.write(data)
        data,addr = s.recvfrom(1024)
    file.close()

