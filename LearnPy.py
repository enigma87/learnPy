from swampy.TurtleWorld import *

'''
world = TurtleWorld()
bob = Turtle()
print bob

for i in range(4):
  fd(bob, 100)
  lt(bob)

wait_for_user()
'''
'''
world = TurtleWorld();
ramu = Turtle();
def square(somu, length):
  for i in range(8):
      fd(somu, length)
      lt(somu)

square(ramu, 50)

wait_for_user();
'''

world = TurtleWorld()
'''
def polygon(somu, length, sides):
    for i in range(sides):
        fd(somu, length)
        rt(somu, 360/sides)

polygon(Turtle(), 2, 180)
'''
from math import *


def circle(somu, radius, angle):
  somu.delay = 0;
  peri = 2 * pi * radius;
  for i in range(angle):
    fd(somu, peri/360)
    rt(somu, 1)

circle(Turtle(), radius=50, angle=90)
wait_for_user();
