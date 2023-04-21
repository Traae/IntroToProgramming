# Project Name: Movie Manager
# CS 1181
# Traae Bloxham
# 11/22/2019
# Brandon Carpenter
# Description - a program for managing a movie collection utilizing classes.

import movie  # my movie class

def main():
    print("Welcome to you Movie Collection")
    movies = []  # create a list that will be made of the movie class instances
    movie_count = 0   # used to count the avalible indexes of the movies list
    quit_program = False     # main menu while loop variable
    while quit_program == False:
        print("Option  \t Command")  # main menu
        print("~~~~~~~ \t ~~~~~~~~")
        print("Add     \t a")
        print("Read    \t r")
        print("Play    \t p")
        print("Quit    \t q")
        menu_option = input("What you  like to do? \n Command: ")

        if (menu_option == 'a') or (menu_option == 'A'):   # create a movie,
            title = str(input('what is the title: '))
            director = str(input('Who directed this film: '))
            year = str(input('What year did it premier: '))
            movies.append(movie.Movie(title, director, year)) # add it too the list
            movie_count += 1  # update movie count for reference else where.

        elif (menu_option == 'r') or (menu_option == 'R'): # read out all the movie class instances
            read_count = 0
            while read_count < movie_count:     # cycle through the movie list and .get_stuff() each one
                movies[read_count].get_stuff()
                read_count += 1

        elif (menu_option == 'p') or (menu_option == 'P'):  # this cycles through each one, looking for a matching title
            what_movie = str(input('What movie do you want to watch?'))
            search_count = 0
            bad_search = 0
            good_search = False
            while search_count < movie_count: # this goes through each
                if what_movie == movies[search_count].search_movie(): # if it finds it, it "plays" it.
                    print('Now playing: ')
                    movies[search_count].get_stuff()
                    good_search = True

                else: # if the search fails, it ups the bad_search count
                    bad_search += 1
                    if (bad_search == movie_count) and (good_search == False):
                        # the bad search message only triggers it nothing was found
                        print("sorry, we do not list that movie")

                search_count += 1  # increment the search count and keep cylcing

        elif (menu_option == 'q') or (menu_option == 'Q'):
            quit_program = True    # quuit the main menu loop, and thus the program
        else:
            print('invalid option, please try again')

main()
# End program