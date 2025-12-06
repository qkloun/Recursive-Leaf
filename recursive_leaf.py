from turtle import *

def draw_leaf_straight(recursion_level, length):
    def branch(length, depth):
        """One branch only"""
        if depth == 0:
            return 
        else:
            forward(length)
            branch(length/2, depth-1)  # forward
            backward(length*1/3)
            left(45)
            branch(length/(5/2), depth-1)  # left side 
            right(90)
            branch(length/(5/2), depth-1)  # right side 
            left(45)
            backward(length*2/3)
    

    branch(length, recursion_level)
    
clearscreen()
speed(0)
tracer(0)
left(90)  # Make it vertical
width(0.1)
draw_leaf_straight(6, 120)
update()
done()

test_make_pairs()


