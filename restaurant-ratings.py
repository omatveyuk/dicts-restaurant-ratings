import sys
import random


def get_ratings():
    """Get restaurant ratings from file.

        file_name: text file which contents names of restaurants and its ratings

    """

    filename = sys.argv[1]
    openfile = open(filename)

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
    while True:
        try:
            score = int(raw_input("Enter rating of restaurant(1-5): \n"))
            break
        except ValueError:
            print "Invalid input. Please enter 1-5"
    rating[name] = score


def pick_choice():
    """Allow user their choice of 3 actions.

        Actions:
        1: see rating
        2: add new rating
        3: quit

    """
#Allow user to choose their action
    while True:
        user_choice = raw_input("\nWould you like to: \n" +
                                "see ratings(Enter 1),\n" +
                                "add new restaurant(Enter 2),\n" +
                                "quit (Enter 3)\n")
        if user_choice == "1" or user_choice == "2":
            run_choice(user_choice)
        elif user_choice == "3":
            print "Goodbye!"
            return
        else:
            print "Make right choice, please"


def run_choice(choice):
    """Call appropriate function based on user choice """
    if choice == "1":
        restaurant_rating = get_ratings()
        print_ratings(restaurant_rating)
    elif choice == "2":
        restaurant_rating = get_ratings()
        add_user_rating(restaurant_rating)
        print_ratings(restaurant_rating)


def give_random_rest():

    #create dictionary
    restaurant_rating = get_ratings()
    #pull a random key, value pair (random choice)
    name = random.choice(restaurant_rating.keys())
    print name, "is rated at", restaurant_rating[name]
    #raw input a new score from user
    while True:
        try:
            score = int(raw_input("Enter rating of restaurant(1-5): \n"))
            break
        except ValueError:
            print "Invalid input. Please enter 1-5"
    #assign new value to key(rest)
    restaurant_rating[name] = score
    #print again
    print_ratings(restaurant_rating)


# pick_choice()
give_random_rest()
