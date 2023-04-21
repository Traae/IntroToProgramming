# Project 4 - Carpet Quote Calculator
# CS 1181
# Traae Bloxham
# 9/13/10
# Brandon Carpenter
# Description - This is 1 of 2 scripts for the project.
# this script will contain functions that perform the
# math needed too run our program

'''
Function Name: convert_inches_to_feet
This function converts inches to feet
'''
def convert_inches_to_feet(width, length):
    width /= 12
    length /= 12
    return width, length


'''
Function Name: calculate_square_footage
betcha can't guess what it does
'''
def calculate_square_footage(width, length):
    square_footage = width * length
    return square_footage


'''
Function Name: calculate_price
calculates the price
'''
def calculate_price(price, square_footage):
    quote_price = price * square_footage
    return quote_price