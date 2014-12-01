# Echo server program
import socket
import random as rand

HOST = ''                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while 1:
    conn, addr = s.accept()
    #print ('Connected by', addr)
    data = "none"
    while 1:
        data = conn.recv(1024).decode("UTF-8")
        if not data:
            break
        print("Received from client:",data)

        user = input()
        #random rgb value
        val = [rand.randint(0,1),rand.randint(0,1),rand.randint(0,1)]
        if user == "halt":
            val = "'halt'"
        d_to_send = val
        conn.send(str(d_to_send).encode("UTF-8"))
        print("sent ",val)
        if val=="'halt'":
            print("stopping")
            conn.close()
            print("Connection closed")
            break



