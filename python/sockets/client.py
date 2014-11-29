# Echo client program
import socket
#192.168.1.5
HOST = '192.168.1.5'    # The remote host
PORT = 50007              # The same port as used by the server

going = True
while going:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    d_to_send = input("Data to send: ")

    s.connect((HOST, PORT))
    s.send(d_to_send.encode("UTF-8"))
    print('sent "'+d_to_send+'"')
    data = s.recv(1024).decode("UTF-8")
    s.close()
    print ('Server says: ', repr(data))
    if d_to_send == "halt":
        going = False
    print()
