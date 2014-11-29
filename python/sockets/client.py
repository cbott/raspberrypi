# Echo client program
#designed to run on Raspberry Pi w/ python 2
import socket

HOST = '192.168.1.15'    # The remote host
PORT = 50007              # The same port as used by the server

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    d_to_send = raw_input("Data to send: ")

    s.connect((HOST, PORT))
    s.send(d_to_send.encode("UTF-8"))
    print('sent "'+d_to_send+'"')
    data = s.recv(1024).decode("UTF-8")
    s.close()
    print 'Server says: ', data
    if data == "halt":
        break
    print
print("connection terminated by server")
