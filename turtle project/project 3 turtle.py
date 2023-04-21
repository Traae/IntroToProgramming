# Project Name: draw your own shape
# CS 1181
# Traae Bloxham
# 9/6/2019
# Brandon Carpenter
# Description - ask the user for information about what they what drawn, then draw it.

import turtle
# import turtle library for use

window = turtle.Screen()
# set window settings for using turtle

paint = turtle.Turtle()
# establish my turtle instance
paint.color("Red")
paint.shape("turtle")
# changed the color and shape for fun.

print("Hello, welcome to Draw-a-shape")
# intro to user
side_num = int(input('How many sides? '))
# prompts for number of sides and assign it to variable "side_num"
side_length = float(input('How long should the sides be? '))
# prompt for length and put it into variable side_length
angles = float(input('How many degrees of each angle? '))
# prompt for angle degrees and assign to variable angles
# we now have all inputs from the user

# start a for loop that will draw the shape
for side_draw in range(side_num):
    # repeat the loop based on the number of sides
    paint.forward(side_length)
    paint.right(angles)
    # move forward, turn, and then repeat




window.exitonclick()
# keep the window open, yo!
# End program.
