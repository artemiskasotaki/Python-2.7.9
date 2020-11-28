class Robot:
    def __init__(self,steps,length):
        self.dist=0
        self.cons=0
        self.steps=steps
        self.length=length

    def display(self):
        print self.dist, self.cons, self.steps, self.length

    def distance(self):
        self.dist=self.steps*self.length

    def energy(self):
        self.cons=10*self.dist/100.0


x1=input("Give Steps for Robot100: ")
m1=input("Give Length of the steps in cm for Robot100: ")
x2=input("Give Steps for Robot101: ")
m2=input("Give Length of the steps in cm for Robot101: ")

Robo100=Robot(x1,m1)
Robo101=Robot (x2,m2)

d1=Robo100.distance()
d2=Robo101.distance()

e1=Robo100.energy()
e2=Robo101.energy()

Robo100.display()
Robo101.display()

if d1>d2:
    print "Robo100 moved with the slowest speed"
else:
    print "Robo101 moved with the slowest speed"
