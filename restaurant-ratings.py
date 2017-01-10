import sys

def restaurant_ratings(file_name):
    """Print restaurant ratings in alphabetical order.

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
    # print ratings

    #sort our dictonary 
        sorted_restaurants = sorted(ratings)

        for restaurant in sorted_restaurants:
            print restaurant, "is rated at", ratings[restaurant]

    openfile.close()


filename = sys.argv[1]
restaurant_ratings(filename)
