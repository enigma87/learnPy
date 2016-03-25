from swampy.TurtleWorld import *;

world = TurtleWorld()

def line(turtle, steps, stepLen, turn):
  for i in range(steps):
    fd(turtle, stepLen)
    rt(turtle, turn)

def regular_polygon(turtle, sides, sideLen):
  line(turtle, sides, sideLen, 360/sides)


from math import *

def arc(turtle, radius, angle):
    turtle.delay = 0
    peri = 2 * pi * radius * (float(angle)/360)
#    print angle
#    print angle/int(angle)
    line(turtle, int(angle), (float(peri)/angle), angle/int(angle))

def circle(turtle, radius):
  arc(turtle, radius, 360)

#def petal(turtle, petal_radius, ):
bob = Turtle()

def petal(radius, turn, overlap):
  arc(bob, radius, turn)
  rt(bob, 180.0 - turn)
  arc(bob, radius, turn)
  rt(bob, 180.0 - 2 * turn + overlap)

def flower(radius, petalNo, overlap):
    for i in range(petalNo):
        petal(radius, 360.0/petalNo + overlap, overlap)


def drawTriangle(jane, side,inner_angle):
  outer_angle = (180.0-inner_angle) / 2.0
  t_h = tan(radians(outer_angle)) * (side/2)
  t_l = sqrt(pow(side/2, 2) + pow(t_h, 2))

  print "height", t_h, "slant", t_l, "base" ,side
  fd(jane, t_l)
  rt(jane, 180 - outer_angle)
  fd(jane, side)
  rt(jane, 180 - outer_angle)
  fd(jane, t_l)
  rt(jane, 180 - 2 * inner_angle)

#drawTriangle(Turtle(), 100, 60);
def turtlePie(jane, slices, size):
  fd(jane, 500)
  for i in range(slices):
      drawTriangle(jane, size, 360.0/slices)

turtlePie(Turtle(), 7, 150)


def spiralchimedes(magic, length):
    magic.delay=0
    skew = 0.0
    for i in range(length * 2):
            fd(magic, 1)
            rt(magic, 5.0 - (skew))
            if (i % 60  == 0):
              skew += 0.2

#spiralchimedes(Turtle(), 500)
pu(bob)
fd(bob, 200)
rt(bob, 90)
fd(bob, 200)
pd(bob)
flower(75, 11, 30)
wait_for_user()
