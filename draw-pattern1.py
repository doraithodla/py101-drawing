
# turtle is a library. It is known as a module in Python
# In the statement below, we are loading all the functions in the turtle module

from turtle import *

# The next few lines define a function. Function is also known as a procedure in some languages
# A function has one or more parameters and sometimes returns a value
# def - is a Python statement to define a function
# shape is the name of the function
# length and sides are parameters (they are place holders). When a function is
# called, the values are substituted for these parameters
# For example shape(100,4) draws a square (sides=4) of length 100 (pixels)
# A function has a header and a body.
# The body in this case consists of three lines (for, fd, lt) below the function definition
# In Python lines of code at the same indentation level is called a block
# In other languages like  C and Javascript a block is enclosed in { and }. 


def shape(length, num_sides):
    # the following code consists of a repeat statement followed by a block of code
    # the number of repetitions are decided by the range(sides). If sides = 4, the block of code
    # is repeated 4 times
    # fd is a short form for forward and lt is a short form for left
    # How the parameters are interpreted is left to the function. For example:
    # length is interpreted by fd as number of pixels
    # 360/sides is interpreted by lt (short form for left) as angle
    angle = 360/num_sides
    for i in range(num_sides):
        fd(length)
        lt(angle)


len_of_side = 100  # Length is known as a variable. 100 is the value assigned to the variable.

#  for sides in range(3,8):
#   shape(length,sides)

# This for loop draws a shape of sides 20 with a length of 20
# It draws this shape 18 times
# After drawing the shape, it tilts the angle by 20 degrees

for count in range(18):
    shape(50, 4)
    lt(20)

"""
Practice Exercise:
1. Un comment the code from line 36 to line 41 and re-run the program 
2. In line 43 and 44 we use numbers like 18 and 20. What are they? What happens if you change one of them or both?

"""