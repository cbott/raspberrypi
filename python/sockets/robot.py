###runs o the Raspberry Pi
###This program will receive input from the computer running controller.py
###and send this data to the arduino
###it is a combination of arduino.py and client.py

from i2c import *
import socket, pickle, time

HOST = '192.168.1.11'    # The remote host
PORT = 50007              # The same port as used by the server

DATA_BITS = 6#bits used as data. must match value on arduino

old_data = [0,0,0,0]

arduino = I2C()

#socket code
print("Creating socket")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Attempting to connect to server")
d_to_send = "Connetction made!"
s.connect((HOST, PORT))
print("Successfully Connected!")
s.send(pickle.dumps(d_to_send))
print('Communicating with server')

#cleanup procedures
def cleanup():
    s.close()
    print("connection terminated by server")

while 1:
    data = pickle.loads(s.recv(1024))
    
    d_to_send = "Pi recieved:"+str(data)
    print(d_to_send)
    
    if data == "halt":#end program if server terminates connection
        break
    
    #run an arduino based on input
    for i in range(len(data)):
        if data[i] != old_data[i]:
            val = combine_bits(DATA_BITS, i+1, data[i])#make id the 1st 4 bits
                                    #and data last 4 bits and limit to 4 bits
            arduino.writeNumber(val)
            print "[RPi] Sent:", val

##	number = arduino.readNumber()
##	print"[Arduino] Received:", number

    old_data = data
    
    s.send(pickle.dumps(d_to_send))

cleanup()
