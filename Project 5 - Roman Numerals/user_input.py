# Project Name - Roman Numerals
# CS 1181
# Traae Bloxham
# 9/20/2019
# Brandon Carpenter
# Description - This will be a program will take input of two numbers, add them, then display a roman numeral
# as an answer. This is the script that will interact with the user and contain my MAIN function.

import roman_numerals  # import my roman numerals module
rome = roman_numerals  # creat an instance of the module names rome fo practice and fun

# The following is the main function ~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    (num_1, num_2) = rome.ask_for_numbers()  # call for the user input function and return the values
    total = rome.add_numbers(num_1, num_2) # call the number adding function and return a total
    rome.numbers_to_roman(total) # call the conversion function and pass it the total

# end main function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

main()  # execute main.
# End program.