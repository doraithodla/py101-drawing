"""
lesson-1 - draw a square
Draws a square of a giVen size
"""

import turtle as t

length = 100
for side in range(4):
    t.forward(length)
    t.right(90)

"""
Exercises
1. Try different values of length
2. Try lt instead of rt
3. Try forward instead of fd
4. Try right instead of lt
"""
