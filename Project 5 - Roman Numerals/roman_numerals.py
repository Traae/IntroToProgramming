# Project Name - Roman Numerals
# CS 1181
# Traae Bloxham
# 9/20/19
# Brandon Carpenter
# Description - This script will contain the functions to add number inputs and "convert"
# numbers to roman numerals.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This function prompts the use to input to values
# and assigns these values to num_1 and num_2 as integers
# it warns the user if the numbers are inappropriate
def ask_for_numbers():
    num_1 = int(input('Enter a number from 1 to 5 '))
    if (num_1 > 5) or (num_1 < 1):
        print('your value is out of my range, your result may fail')
    num_2 = int(input('Enter a number from 1 to 5 '))
    if (num_2 > 5) or (num_2 < 1):
        print('your value is out of my range, your result may fail')
    return num_1, num_2
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This functions adds to passed in values together as integers
# it also checks the value to see if its in range.
def add_numbers (num_1, num_2):
    num_total = int(num_1) + int(num_2)
    return num_total
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This function will take the passed number
# and print the corresponding roman numeral
def numbers_to_roman(number):

    # This series of if statement mamually checks each possible value
    # then prints the output in text.
    if number == 1:
        print("You value is I")
    elif number == 2:
        print("You value is II")
    elif number == 3:
        print("You value is III")
    elif number == 4:
        print("You value is IV")
    elif number == 5:
        print("You value is V")
    elif number == 6:
        print("You value is VI")
    elif number == 7:
        print("You value is VII")
    elif number == 8:
        print("You value is VIII")
    elif number == 9:
        print("You value is IX")
    elif number == 10:
        print("You value is X")
    elif number < 1:
        print("You value is too low.")
    elif number > 10:
        print('you value is too high.')
    # the final 2 statements evaluate exceptions to the programs scope of function
    # and display a corresponding message
    # there must be a better way to do this. However we learned if statments this week soooooooooooo, yeah.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# End script.