"""
lesson-4 - draw two shapes at two locations.
"""
import turtle as t


def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


sides, length = 4, 50  # Notice that we can assign multiple variables with one statement.

angle = 360/sides

for side in range(sides):
    t.fd(length)
    t.rt(angle)

move(-100, 100)
for side in range(sides):
    t.fd(length)
    t.rt(angle)

""" Exercises
1. Accept the x,y co-ordinates from the user and draw the square there. 
2. Draw a house at a gvien x, y co-ordinates. A house is a triangle on top of a square
3. Draw a colored house (brown body, red roof)
"""
