# Project Name: Dart board Game
# CS 1181
# Traae Bloxham
# 9/27/2019
# Brandon Carpenter
# Description - A Dart board game following the "Standard 01" game
# sooooo, I tried to implment a bunch of stuff, but I'm drowning in homework.
# I cut this back to be barebones.

import random

# this function throws a dart, and returns the appriate score number.
# it also prints a message on special values such as bull, bulls eye, and bust
def throw_a_dart():
    dart_hit = random.randint(0, 23)  # 1 for each area of the dart board, and 0 for a miss/bust
    dart_score = 0
    # 21 and 22 will be the bulls eye and bull, any other number has a bonus chance
    if dart_hit == 0:
        dart_score = dart_hit
        print('bust!')
    elif dart_hit == 21:
        dart_score = 50
        print('Bulls Eye!')
    elif dart_hit == 22:
        dart_score = 25
        print('Bull!')
    else:
        dart_score = dart_hit
        bonus_chance = random.randint(1, 21)  # this gve 1/20 = 5% chance of a triple, and 10% of a double
        if bonus_chance == 1:
            dart_score = dart_score * 3
            print('Tripled!')
        elif (bonus_chance == 2) or (bonus_chance == 3):
            dart_score = dart_score * 2
            print('Doubled!')
    return (dart_score)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# This function checks the value of the score in case of a negative score
# otherwise it deducts the dart score from the total
def score_calculator(total, dart_score):
    if (total - dart_score) < 0:
        print('Too Low! Try again')
    else:
        total -= dart_score
    return(total)

# This function will execute a normal game as required by the assignment.
def play_standard_01_game(starting_score):
    print('The starting score is ', starting_score)
    game_finish = False  # establish while loop variable
    throw_count = 0  # establish the throw count outside of the while loose
    total = starting_score  # total score to play from

    print('Hit \t Total \t Throw')  # start a nice little table for score keeping
    print('~~~ \t ~~~~~ \t ~~~~')
    # repeatedly use the throw dart function, display the new statistics, and check to see
    # if the game should end.
    while game_finish == False:
        dart_score = throw_a_dart()
        total = score_calculator(total, dart_score)
        throw_count += 1
        print(dart_score, '  \t', total, '  \t', throw_count)
        if total == 0:
            game_finish = True
            print('Congratulations. You finished in ', throw_count, ' throws.')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# My main function to replay the game
def main():
    play_again = True  # bool to set up a replay loop
    print('Welcome to Darts')
    print('We can play an 01 game')
    while play_again == True:
        print('Normally you start from 301 0r 501')
        starting_score = int(input('What score will you start from?'))  # ask the users for a starting score
        # the score can be anything, but the program will tell the user when they've broken the usual rules
        if (starting_score != 301) and (starting_score != 501):
            print('That is a bit silly, but okay')
        play_standard_01_game(starting_score)
        replay = input('would you like to play again? y/n')
        if replay == 'n':
            play_again = False
        elif replay == 'y':
            play_again == True
        else:
            print('I did not understand that, so I quit')
            play_again = False

main()

# end program