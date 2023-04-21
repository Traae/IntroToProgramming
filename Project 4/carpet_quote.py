# Project 4 - Carpet Quote Calculator
# CS 1181
# Traae Bloxham
# 9/13/10
# Brandon Carpenter
# Description - This is 2 of 2 scripts for the project.
# this script will contain the prompts for user interaction
# and the outputs for their price quote, and our  main function and logic

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function Name: ask_for_info
# this function will ask for the demensions of the carpet

def ask_for_info(carpet_number):
    # the folowing three questions will promt for the data we need

    width_inches = float(input('Carpet #' + str(carpet_number + 1) + ' width in inches:'))
    # make and prompt for width_inches and make it a float

    length_inches = float(input('Carpet #' + str(carpet_number + 1) + ' length in inches:'))
    # make and prompt for lenght_inches and make it a float

    price = float(input('Carpet #' + str(carpet_number + 1) + ' price per square foot:'))
    # make and prompt for price and make it a float

    return(width_inches, length_inches, price)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import price_calculator
# import our price calculator script/module for use



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function name: do_da_math
# this fucntion will take all of our gathered info and return the price
def do_da_math(width_inches, length_inches, price):

    # pass width_inches and length_inches in to have them converted, pass back the values
    # for the new variables width and length
    (width, length) = price_calculator.convert_inches_to_feet(width_inches, length_inches)

    # pass in width and length and get back the value for the new variable square_footage
    square_footage = price_calculator.calculate_square_footage(width, length)

    # finally pass the price variable and square_footage  to calculate the quote price
    quote_price = price_calculator.calculate_price(price, square_footage)

    return quote_price
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






# This is my main function for running the program
def main():
    number_of_carpets = int(input('Welcome to the Carpet Quote Program! \nHow mayn types of carpet are we looking at today? '))
    #this statement creates and asks for the number oof carpets and give it a variable

    # global variable for cross function use
    width_inches = 0.0
    length_inches = 0.0
    price = 0.0
    quote_price = 0.0
    total_price = 0.0

    # a for loop for all the carpet questions, respective math, and print the quote for each carpet
    for carpet_number in range(number_of_carpets):

        # Call ask_for_info and return the variables to
        (width_inches, length_inches, price) = ask_for_info(carpet_number)

        # pass in all my data to do_da_math to get the quote price
        quote_price = do_da_math(width_inches, length_inches, price)

        total_price += quote_price
        # add the quote price to the total price

        # finally we print the price
        print('The price for Carpet #' + str(carpet_number + 1) + ' is: $' + str(round(quote_price, 2)))

    # we are now out of the for loop

    print('The total cost for the carpet is: $' + str(round(total_price, 2)))
    # print the final total

# End main function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`

main()

# End program.
