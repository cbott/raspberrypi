from Tkinter import *
import motorLib


right = motorLib.Motor()
left = motorLib.Motor(12,16,18,22)

root = Tk()

def key(event):
    letter = event.char
    if letter == 'w':
        print "up"
        left.fwd()
        right.fwd()
    elif letter == 'a':
        print "left"
        left.rev()
        right.fwd()
    elif letter == "d":
        print "right"
        left.fwd()
        right.rev()
    elif letter == "s":
        print "down"
        left.rev()
        right.rev()
    else:
        print "stop"
        left.stop()
        right.stop()

def callback(event):
    frame.focus_set()
    print "Begin!"

frame = Frame(root, width = 100, height = 100)
frame.grid()
Label(frame, text = "Use  'w' 'a' 's' 'd'  to move").grid()

#frame.bind("<Button-1>", callback)
frame.bind("<Key>", key)


frame.pack()
frame.focus_set()
root.title("RC Car")
root.mainloop()
