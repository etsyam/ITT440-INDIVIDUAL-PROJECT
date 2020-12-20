import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host =sys.argv[1]
port = 6789

addr = (host,port)

file_name=sys.argv[2]

s.sendto(file_name.encode(),addr)

file = open(file_name,"rb")
data = file.read(1024)

while (data):
    if(s.sendto(data,addr)):
        data = file.read(1024)
s.close()
file.close()
