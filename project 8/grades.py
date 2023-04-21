# Project Name: Grades
# CS 1181
# Traae Bloxham
# 10/25/2019
# Brandon Carpenter
#  Description - This program will randomly generate "grades" for a class
#  then store them in a tuple, and then print them out to the user.

import random  # import the random module

# define my main function for easy of repeated execution
def main():
    grades_list = [] # establish my list of grades, global from the while that will fill it up
    # establish the min, max, and average values
    min_grade = 100.00
    max_grade = 50.00
    average_grade = 0
    grade_generator_count = 0       # create a counter and while loop to generat 35 results
    while grade_generator_count < 35:
        new_grade = round(random.uniform(50, 100), 2)   # the results are random between 50 and 100 rounded to 2 decimals
        # the following if statements will determine an approppriaptt letter grade correspoding to the new_grade value
        if new_grade < 60:
            new_letter_grade = "F"
        elif new_grade <= 62.99:
            new_letter_grade = "D-"
        elif new_grade <= 66.99:
            new_letter_grade = "D"
        elif new_grade <= 69.99:
            new_letter_grade = "D+"
        elif new_grade <= 72.99:
            new_letter_grade = "C-"
        elif new_grade <= 76.99:
            new_letter_grade = "C"
        elif new_grade <= 79.99:
            new_letter_grade = "C+"
        elif new_grade <= 82.99:
            new_letter_grade = "B-"
        elif new_grade <= 86.99:
            new_letter_grade = "B"
        elif new_grade <= 89.99:
            new_letter_grade = "B+"
        elif new_grade <= 92.99:
            new_letter_grade = "A-"
        elif new_grade <= 100:
            new_letter_grade = "A"

        # check to see if there is a new minimum grade
        if new_grade < min_grade:
            min_grade = new_grade
        # check and change for max grad
        if new_grade > max_grade:
            max_grade = new_grade
        average_grade += new_grade  # add the grades together to be calculated later

        new_grade_tuple = (new_grade, new_letter_grade)
        grades_list.append(new_grade_tuple)
        grade_generator_count += 1
    average_grade = round((average_grade / 35), 2) # finish the average calculation
    # the following will print ass the steez
    print('Grades for Applied Sex Education')
    print('Numeric grade (%) \t Letter Grade')
    # the for loop will cycle thourgh to hit and print each line
    index_count = 0
    for grade in grades_list:
        print(grades_list[index_count][0], "   \t          ", grades_list[index_count][1])
        index_count +=1
    print("Minimum Grade: ", min_grade)
    print("Maximum Grade: ", max_grade)
    print("Average Grade: ", average_grade)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`


# a simple while loop for repeated execution of the main function
cont_yn = "y"
while cont_yn == "y":
    main()
    cont_yn = input("Would you like to run the program again? y/n: ")
# end program