import turtle
import math
bob = turtle.Turtle()

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

def squarel(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)

def circle(t, r):
    arc(t, r, 360)

def circle2(t,r):
    circumference = 2 * math.pi * r
    n = int(circumference/3) + 1
    length = int(circumference/n)
    polygon(t, n, length)

def polyline(t,n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r *angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle =float(angle)/n
    polyline(t, n, step_length, step_angle)

polyline(bob, 80, 200, 5)

turtle.mainloop()
