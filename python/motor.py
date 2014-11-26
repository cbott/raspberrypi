import motorLib

m1 = motorLib.Motor()
m2 = motorLib.Motor(12,16,18,22)
#EXPLODE!!!!!!!!!!!
m1.fwd()
m2.fwd(2)

m1.stop()
m2.stop()

m1.rev()
m2.rev(2)

m1.stop()
m2.stop()
