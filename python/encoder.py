from encoder_class import RotaryEncoder

A1PIN = 11
B1PIN = 12
BUTTON1 = 13

A2PIN = 15
B2PIN = 16
BUTTON2 = 18

def lrevents(val):
    if val == 1:
        print("right")
    elif val == 2:
        print("left")
    elif val == 3:
        print("lr button")
    else:
        pass
def udevents(val):
    if val == 1:
        print("down")
    elif val == 2:
        print("up")
    elif val == 3:
        print("ud button")
    else:
        pass
    
encoder1 = RotaryEncoder(A1PIN, B1PIN, BUTTON1, lrevents)
encoder2 = RotaryEncoder(A2PIN, B2PIN, BUTTON2, udevents)

while 1:
    pass


    
        
