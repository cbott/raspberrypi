# Echo client program
#designed to run on Raspberry Pi w/ python 2
import socket

HOST = '192.168.1.15'    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

d_to_send = "Connetction made!"
s.connect((HOST, PORT))
s.send(d_to_send.encode("UTF-8"))
print('Attempted to make connection')
data = s.recv(1024).decode("UTF-8")

while 1:
    data = s.recv(1024).decode("UTF-8")
    d_to_send = "Pi recieved:"+data

    print(d_to_send)
    #s.connect((HOST, PORT))
    s.send(d_to_send.encode("UTF-8"))
    
    if data == "halt":
        break
    print

s.close()
print("connection terminated by server")
