import sys


def get_ratings(file_name):
    """Get restaurant ratings from file.

        file_name: text file which contents names of restaurants and its ratings

    """

    openfile = open(file_name)

    ratings = {}

    # split line into lists
    for line in openfile:
    #unpack list to 2 variables
        name, rating = line.rstrip().split(':')

    #assign variables to key value pairs
        ratings[name] = rating

    openfile.close()
    return ratings


def print_ratings(rating):
    """Print sorted rating"""

    #sort our dictonary
    sorted_rating = sorted(rating)

    for restaurant in sorted_rating:
        print restaurant, "is rated at", rating[restaurant]


def add_user_rating(rating):
    """get new rating from user and add to existing ratings"""

    name = raw_input("Enter name of restaurant: \n")
    score = int(raw_input("Enter rating of restaurant(1-5): \n"))
    rating[name] = score
  

filename = sys.argv[1]
restaurant_rating = get_ratings(filename)
# call function to print ratings
print_ratings(restaurant_rating)

add_user_rating(restaurant_rating)
print_ratings(restaurant_rating)
