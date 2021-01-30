"""
lesson-3 - ask user what shape to draw and draw that shape
In this program, we ask the user to give us the number of sides
the int function converts the string typed by the user into an integer
"""

import turtle as t

sides = int(input("Enter the number of sides: "))
length = 200
angle = 360/sides

for side in range(sides):
    t.fd(length)
    t.rt(angle)

""" Exercises
1. Try different shapes
2. Modify the program to accept sides and length from the user and draw a shape of that length
"""
