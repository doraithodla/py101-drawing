"""
lesson-5 - draw and fill a shape with color
"""
import turtle as t

t.color('black', 'red')

t.begin_fill()

length, sides = 100, 4
angle = 360/sides

for side in range(sides):
    t.fd(length)
    t.rt(angle)
    
t.end_fill()
t.done()

""" Exercises
1. Draw multiple squares with different colors
2. Comment t.done() and run the program and see what happens
3. Draw different shapes with different fill colors
"""
