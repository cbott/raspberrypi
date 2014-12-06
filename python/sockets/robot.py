###This program will receive input from the computer runnin controller.py
###and send this data to the arduino
###it is a combination of arduino.py and client.py

from i2c import *
import socket, pickle, time

HOST = '192.168.1.2'    # The remote host
PORT = 50007              # The same port as used by the server

DATA_BITS = 4#bits used as data. must match value on arduino

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

while 1:
    data = pickle.loads(s.recv(1024))
    
    d_to_send = "Pi recieved:"+str(data)
    print(d_to_send)
    commands = data
    #run an RGB LED based on input
    for i in range(3):
        val = combine_bits(DATA_BITS, i+1, data[i])#make id the 1st 4 bits
                                    #and data last 4 bits and limit to 4 bits
	arduino.writeNumber(val)
	print "[RPi] Sent:", val
	time.sleep(0.05)
	number = arduino.readNumber()
	print"[Arduino] Received:", number

    #print(d_to_send)
    s.send(pickle.dumps(d_to_send))
    
#cleanup procedures
s.close()
print("connection terminated by server")
