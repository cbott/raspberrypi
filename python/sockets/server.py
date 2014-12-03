# Echo server program
import socket, pickle
import random as rand

HOST = ''                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)

while 1:
    conn, addr = s.accept()
    #print ('Connected by', addr)
    data = "none"
    while 1:
        data = pickle.loads(conn.recv(1024))
        if not data:
            break
        print("Received from client:",data)

        user = input()
        #random rgb value
        val = [rand.randint(0,1),rand.randint(0,1),rand.randint(0,1)]
        if user == "halt":
            val = "halt"
        d_to_send = val
        conn.send(pickle.dumps(d_to_send, protocol=2))
        print("sent ",val)
        if val=="halt":
            print("stopping")
            conn.close()
            print("Connection closed")
            break



