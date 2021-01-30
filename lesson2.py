"""
lesson-2 - draw a shape
Draws a shape (triangle, square, pentagon etc.)
"""

import turtle as t

length = 100
sides = 5
angle = 360/sides

for side in range(sides):
    t.fd(length)
    t.rt(angle)

"""
Exercises
1. Try different shapes
2. Try different shapes of various sizes
"""