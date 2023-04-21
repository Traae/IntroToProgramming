# This is my class for the movie manager program
class Movie:   # initilize da class.
    def __init__(self, title_value, director_value, year_value):   # set up to passin the value upon creation
        self.title = title_value
        self.director = director_value
        self.year = year_value

    def get_stuff(self):   # this function prints info about the movie
        print(self.title, ', Directed by ', self.director, ' premiered in ', self.year)

    def search_movie(self): # this is pretty much just a getter for the title, used for the play function
        return self.title

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~