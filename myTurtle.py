from swampy.TurtleWorld import *;

world = TurtleWorld()

def line(turtle, steps, stepLen, turn):
  for i in range(steps):
    fd(turtle, stepLen)
    rt(turtle, turn)

def polygon(turtle, sides, sideLen):
  line(turtle, sides, sideLen, 360/sides)


from math import pi

def arc(turtle, radius, angle):
    turtle.delay = 0
    peri = 2 * pi * radius * (float(angle)/360)
    print angle
    print angle/int(angle)
    line(turtle, int(angle), (float(peri)/angle), angle/int(angle))

def circle(turtle, radius):
  arc(turtle, radius, 360)

#def petal(turtle, petal_radius, ):
bob = Turtle()

def petal(radius, turn, overlap):
  arc(bob, radius, turn)
  rt(bob, 180 - turn)
  arc(bob, radius, turn)
  rt(bob, 180 - 2 * turn + overlap)

def flower(radius, petalNo, overlap):
    for i in range(petalNo):
        petal(radius, 360/petalNo + overlap, overlap)


flower(300, 11, 30)
wait_for_user()
