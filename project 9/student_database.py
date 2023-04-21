# Project Name: Student database
# CS 1181
# Traae Bloxham
# 11/055/2019
# Brandon Carpenter
# Description - A program that can read, add to, and delete from a text file of student information.

def createfile():   # this function creates the txt file that we are using just for ease of transfer to Blaise, and formatting
    writefile = open("studentList.txt", 'w')
    writefile.write(
        "1,John,Jacobson,GOTHIC\n"
        "2,Jacob,Jensen,COSMIC\n"
        "3,Jen,Jackson,BODY\n"
        "4,Jacklyn,Johnson,SURREAL")
    writefile.close()

def add_student():    # this function will opne the text file and append a student to the end
    writefile = open("studentList.txt", 'a')
    newstudent = input("What is the student's ID number?")    # it asks for the values, and store them in sting
    newstudent = newstudent + ','     # then adds a comma, as per the file's formatting
    newstudent = newstudent + input("What is the student's first name?")   # lather, rinse, repeat
    newstudent = newstudent + ','
    newstudent = newstudent + input("What is the student's last name?")
    newstudent = newstudent + ','
    newstudent = newstudent + input("What is the student's Major?")
    writefile.write('\n' + newstudent)  # finally add a newline character to stirng so it will go to the line below
    writefile.close()

def read_student():
    readfile = open("studentList.txt", 'r')   # open the file for reading
    for line in readfile:    # read the lines individually in a for loop
        this_line = line.split(',')  # creat a list of the values in the line, split by the comma
        print(this_line[0], '\t', this_line[1], '\t', this_line[2], '\t', this_line[3].replace("\n", ""))
    readfile.close()

def del_student():
    readfile = open("studentList.txt", 'r')  # open the file to read
    student_Data_Dictionary = {}   # intitialize my dictioary

    for line in readfile: # For loop will read each line
        line_info_list = line.split(",")  # creat a list of the line's info
        ID = line_info_list[0]  # Create a variable that equals the student ID in the file
        student_Data_Dictionary[ID] = line_info_list  # sets the dictionary key to ID and the definition value to the list of info
    readfile.close()

    delete_complete = False
    while delete_complete == False:
        try: # because trying to delete a non existent key value throws an error, this section is in a simple try/except
            student_to_delete = input('What is the ID of the student you want to delete?: ')  # ask for the id
            del student_Data_Dictionary[student_to_delete]  # delete it
            delete_complete = True
        except:
            print("That did not work. please try again")
        # I know I want to learn try/except as more than an if/else, but this if/else logic for and exeotion, sooooo, this is right, right?


    writefile = open("studentList.txt", 'w') # i open and close the file just to clear it.
    writefile.close()   # I'm sure there's a function somewhere, but I'm trying to only use the book,
    # and this take 2 lines of code, soooooo bite me.

    writefile = open("studentList.txt", 'a')
    for entry in student_Data_Dictionary:
        textentry = "," # set a string to the comma to speratate the data
        textentry = textentry.join(student_Data_Dictionary[entry]) # join the list at Dictionary key [entry] into the string textentry
        writefile.write(textentry)
    writefile.close()


def main():
    Quit = False  # while loop set to the quit bool
    while Quit == False:
        print('Welcome to Student Database') # Main menu, it asks for capital letters
        print('What would you like to do')
        print('Option    \t Enter')
        print('Read student \t R')
        print('Add student  \t A')
        print('Delete Student\t D')
        print('Quit         \t Q')
        menu_option = input('?: ')
        if (menu_option == 'r') or (menu_option == 'R'):    # BUT it will accept either case of letter
            read_student()
        elif (menu_option == 'a') or (menu_option == 'A'):
            add_student()
        elif (menu_option == 'd') or (menu_option == 'D'):
            del_student()
        elif (menu_option == 'q') or (menu_option == 'Q'):
            Quit = True
        else:
            print("Sorry, I didn't catch that, please try again")    # repeat is incorrect value


createfile() # creeate the file, so you don't have to worry about
main() # do the thing
# End program