# Echo client program
#designed to run on Raspberry Pi w/ python 2
import socket
import RPi.GPIO as gpio

HOST = '192.168.1.15'    # The remote host
PORT = 50007              # The same port as used by the server

####setup code
gpio.setmode(gpio.BOARD)
RED_PIN = 11
GREEN_PIN = 12
BLUE_PIN = 13
gpio.setup(RED_PIN, gpio.OUT)
gpio.setup(BLUE_PIN, gpio.OUT)
gpio.setup(GREEN_PIN, gpio.OUT)
gpio.output(RED_PIN, True)
gpio.output(GREEN_PIN, True)
gpio.output(BLUE_PIN, True)

#socket code
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

d_to_send = "Connetction made!"
s.connect((HOST, PORT))
s.send(d_to_send.encode("UTF-8"))
print('Attempted to make connection')

while 1:
    data = s.recv(1024).decode("UTF-8")
    d_to_send = "Pi recieved:"+data
    
    commands = eval(data)
    #run an RGB LED based on input
    r = False
    g = False
    b = False
    if commands[0]:
        r = True
    if commands[1]:
        g = True
    if commands[2]:
        b = True
    gpio.output(RED_PIN, not (r))
    gpio.output(GREEN_PIN, not(g))
    gpio.output(BLUE_PIN, not(b))

    #print(d_to_send)
    s.send(d_to_send.encode("UTF-8"))
    
    if data == "halt":
        break

#cleanup procedures
s.close()
print("connection terminated by server")

gpio.output(RED_PIN, True)
gpio.output(GREEN_PIN, True)
gpio.output(BLUE_PIN, True)
gpio.cleanup()

