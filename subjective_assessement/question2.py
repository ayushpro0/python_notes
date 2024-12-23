# Menu Driven Movie Management
#
# Write a menu driven program to add a movie, list all movies and find movie by property. Each movie is a dictionary. Keys are 'name', 'director' and 'year'.
# [Note: Certain property may retrieve multiple movies.]
#
# Input and Output Format:
# Refer Sample Input and Output
#
# Sample Input and Output:
#
# Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:
# a
# Enter the movie name:
# Tenet
# Enter the movie director:
# Christopher Nolan
# Enter the movie release year:
# 2020
#
# Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:
# l
# Name: Tenet
# Director: Christopher Nolan
# Release year: 2020
#
# Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:
# a
# Enter the movie name:
# Iron Man 3
# Enter the movie director:
# Shane Black
# Enter the movie release year:
# 2013
#
# Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:
# l
# Name: Tenet
# Director: Christopher Nolan
# Release year: 2020
# Name: Iron Man 3
# Director: Shane Black
# Release year: 2013
#
# Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:
# f
# What property of the movie is that?
# name
# What are you looking for?
# Tenet
# Movies Details:
# Name: Tenet, Director: Christopher Nolan, Release year: 2020
#
# Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:
# a
# Enter the movie name:
# The Courier
# Enter the movie director:
# Dominic Cooke
# Enter the movie release year:
# 2020
#
# Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:
# f
# What property of the movie is that?
# year
# What are you looking for?
# 2020
# Movies Details:
# Name: Tenet, Director: Christopher Nolan, Release year: 2020
# Name: The Courier, Director: Dominic Cooke, Release year: 2020
#
# Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:
# f
# What property of the movie is that?
# director
# What are you looking for?
# James Cameron
# No movies found.
#
# Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:
# q

movies = []


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:\n")

    while user_input != "q":

        if user_input == 'a':
            add_movie()

        elif user_input == 'l':
            show_movies()

        elif user_input == 'f':
            finder = input("What property of the movie is that?\n")
            expected = input("What are you looking for?\n")
            find_movie(expected, finder)

        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:\n")


def add_movie():
    movie_name = input("Enter the movie name:\n")
    movie_director = input("Enter the movie director:\n")
    movie_year = input("Enter the movie release year:\n")
    temp_dict = {"name": movie_name, "director": movie_director, "year": movie_year}
    movies.append(temp_dict)


def show_movies():
    for movie in movies:
        print("Name:", movie["name"])
        print("Director:", movie["director"])
        print("Release year:", movie["year"])


def find_movie(expected, finder):
    movie_found = []

    for movie in movies:
        if movie[finder] == expected:
            movie_found.append(movie)

    if len(movie_found) == 0:
        print("No movies found.")
    else:
        print("Movie Details:")
        for movie in movie_found:
            show_movie_details(movie)


def show_movie_details(movie):
    print("Name:", movie["name"], ", Director:", movie["director"], ", Release year:", movie["year"])


menu()
