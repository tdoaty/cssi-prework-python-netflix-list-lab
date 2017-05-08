#1. Define a function first_movie that return the first movie in the queue
# This function should accept an list as an argument (the movie queue)
movie_queue = []
def first_movie(movie_queue):
    return first_movie[0]

#2. Define a function watch_next_movie that deletes the first movie in the list and returns the modified list
#This function should accept an list as an argument (the movie queue)
def watch_next_movie(movie_queue):
    movie_queue.pop()
    return watch_next_movie
#3. Define a function add_to_queue that returns the updated list
# This function takes two arguments (the list of movies and the movie you want to add to the end of the queue)
def add_to_queue(movie_queue, new_movie):
    movie_queue.append()
    return add_to_queue
#4. Define a function view_queue that uses a for loop to iterate over the list of movies and return them as a numbered list starting at 1, with a new line for each movie.
def view_queue():
    for movie in movie_queue:
        print "{}." .format(movie)
