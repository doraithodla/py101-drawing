"""
lesson 6 - generates random sized squares in random locations
"""

from turtle import *
from random import randint  # randint is a function to generate a random number.

""" Move the turtle to specified co-ordinaetes"""
def move(x_coord, y_coord):
    penup()
    goto(x_coord, y_coord)
    pendown()

""" Draw a shape at specificed co-ordinates"""
def shape(side, num_sides):
    angle = 360/num_sides
    for n in range(num_sides):
        fd(side)
        lt(angle)


for i in range(10):
    x, y = randint(-200, 200), randint(-200, 200)
    length, sides = randint(10, 100), randint(3, 6)
    move(x, y)
    shape(length, sides)

"""
Practice Exercise:
1. Draw ony squares and triangles
2. Draw a house (a triangle on top of a square)
3. So far we have drawn only regular shapes (like square). Can you write a function to draw a rectangle?
4. Draw a horizontal line at x,y of length l
5. Draw a horizontal line given x1, y1 and x2, y2
6. Draw a vertical line given x1,y1 and x2,y2
7. Draw a grid (a table with rows and columns) given x1,y1 and x2, y2
8. Draw an empty chess board (it is an 8 by 8 grid with alternate colors for each block inside the grid
9. Can you prove that the sum of the squares of a 4 by 4 grid is equal to the total area of the enclosing square
10. Draw only squares and make sure that no two shapes overlap
"""