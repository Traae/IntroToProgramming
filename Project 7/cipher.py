# Project Name:
# CS 1181
# Traae Bloxham
# 10/04/2019
# Brandon Carpenter
# Description - Ceasar cipher thing

import random

def get_key():    # this function wil ask for, and calculate if needed, the cipher key
    print('Enter a number, 0 - 25 for you key, or 100 for random.')  # instructions for user input
    print('Any other number will be modified by a value of 26 until it is acceptable')
    key = int(input('Enter Here: '))

    if key == 100:  # key - 100 will equal a random int in range 0 to 25
        key = random.randint(0, 26)
        print("Your key value is: ", key)  # print new value
    elif key < 0:  # a negative key will take additions of 26 until it's in range
        while key < 0:
            key += 26
            if key <= 0:
                print("Your key value is: ", key)  # print new value
    elif key > 25:  # an excessive key will be reduced by 26 until its in range, save 100, which is checked first
        while key > 25:
            key -= 26
            if key <= 25:
                print("Your key value is: ", key)  # print new value
    return key

def get_string():
    good_string = False  # a while loop and variable to check if the input is good or not
    while good_string == False:
        print("Now, let's choose something to encrypt")   # give string instructions and ask for it
        print("Please enter a a word, or phrase that contains no numbers or symbols.")
        print("It must be less be no more than 250 characters.")
        print("You can enter Upper or lowercase, but I'm only going to give you lowercase letters.")
        user_input_string = str(input("Enter here: "))
        user_input_string= user_input_string.lower()  # convert it to lowercase

        count = 0  # this for loop will count to see if we are in range and check the characters
        for achar in user_input_string:
            check_character = int(ord(user_input_string[count]))   # get the vaule
            if (check_character < 97) or (check_character > 122):   # then if it's not a letter
                if (check_character != 32):                         # then is its not a space
                    print("Sorry, that won't work")
                    good_string = False
                    break                                           # break the for loop
                else:
                    good_string = True                  # otherwise good string will be true when it finishes
            else:
                good_string = True
            count += 1   # add + 1 to the count then check it
            if count == 250:
                print("sorry that's too long")
                good_string = False
                break
    return user_input_string


def enCRYPT_KeyPER(key, user_input_string):    # this will do all the work cipherizing the string
    output_string = ""  # set up the output as nothing
    count = 0      # a count that will incriment in the for loop
    for each_char in user_input_string:
        if int(ord(user_input_string[count])) == 32:     # this will take care of spaces
            output_string = output_string + " "
        else:
            character_number = int(ord(user_input_string[count])) - 97    # takes the value, reduces it to 0 - 25
            character_number = character_number + key            # modifies it with the key
            if character_number > 25:                         # in case it goes over reset the count
                character_number = character_number - 26
            character_number += 97                          # and the value back to corresponde to ord value
        output_string = output_string + chr(character_number)    # adds the next characters to the string
        count += 1
    print('Your encryption is: ', output_string)


def main():
    keep_going = 0
    while keep_going == 0:
        print("Hello, User, let's encrypt some junk with a Ceaser Cipher")  # introduction
        key = get_key()
        user_input_string = get_string()
        enCRYPT_KeyPER(key, user_input_string)
        repeat_program_value = input("Do you want to go again? y/n: ")
        if repeat_program_value == "n":
            keep_going = 1

main()
# end program