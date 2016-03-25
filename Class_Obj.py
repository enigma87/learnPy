#!/usr/bin/python
'''class Point(object):
       x
    y
    def setX(x_val):
        x = x_val
    def setY(y_val):
        y = y_val

p1 = Point()
#p1.setX(5)
#p1.setY(10)
p1.x = 5
p1.y = 5

p2 = Point()
p2.p = Point()
p2.p.x = 5
p2.p.y = 10


import math
def distance(P1, p2):
    return math.sqrt( (p1.x-p2.p.x)**2 + (p1.y-p2.p.y)**2 )


print distance(p1,p2)
'''


from swampy.World import *

world = World()

canvas = world.ca(width=500, height=500, background='white')

bbox=[[-150, -100], [150, 100], [150, -100]]

canvas.polygon(bbox, outline='pink', width=5, fill='green4')
canvas.circle([250, 0], 75, outline='blue', width=2, fill='pink')

world.mainloop()
