# Echo server program
import socket

HOST = ''                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while 1:
    conn, addr = s.accept()
    #print ('Connected by', addr)
    #print()
    data = "none"
    while 1:
        data = conn.recv(1024).decode("UTF-8")
        if not data:
            break
        print("Received from client:",data)
        #d_to_send = "I received '"+data+"' from client"
        val = input("Reply: ")
        d_to_send = val
        conn.send(d_to_send.encode("UTF-8"))
        if val=='halt':
            print("stopping")
            conn.close()
            print("Connection closed")
            break



