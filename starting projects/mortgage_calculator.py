# Project 2 - Mortgage Calculator
# CS 1181
# Traae Bloxham
# 8/26/2019
# Brandon Carpenter
# Description - To create a simply mortgage calculator.

print('Hello, welcome to monthly payment calculator.')
# I need an intro to feel complete

home_cost = float(input('Please enter the cost of your home? $'))
# declare home_cost, ask for it's value, and convert it to a float for caculations.

interest_rate = float(input('Please enter the annual interest rate? %'))
# prompt the users for interest rate, convert to float and assign value to variable.


loan_term = int(input('Please enter the length of the loan in months: '))
# prompt for loans months, convert it to a float, and assign to variable laon_term.

interest_calc = float((interest_rate / 100) / 12)
# changing interest_rate to a decimal number for calculations - assinged to interest_calc

payment = home_cost * ((interest_calc * ((interest_calc + 1)**loan_term))  /  (((1 + interest_calc)**loan_term) - 1))
# create the variable payment and assign it the appropriate value calculated based on the monthly payment formula

print("You mortgage payment will be $" + str(round(payment, 2)))
#display the monthly payment in dollars and cents

# End program.
