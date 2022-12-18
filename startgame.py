# CSS 225 Final Project
# Author: Victoria Price
# Date: 12/10/2022

# A program that contains the function that welcomes
# the user and asks if they are ready to play.

import time  # imports the time library from Python
import globalvariables  # imports all of my global variables


# a function that welcomes the user to the game
def start_up():

    # welcome message that asks the user to enter their name
    globalvariables.player_name = input("Welcome to ABANDONED, the best text-based RPG of 2022. "
                                        "\nWhat would you like to be called?: ")

    # greet the user by their name
    print(f"Nice to meet you, {globalvariables.player_name}.")

    # ask the user if they are ready to play
    ready_to_start = input("Are you ready to begin playing? "
                           "Enter YES or NO: ").upper()

    begin_game = False

    # if the user enters "NO" because he/she is not ready to play,
    if ready_to_start == "NO":
        # print a message that tells the user to come back later
        print("That's a shame. Please come back soon!")
        begin_game = False
        time.sleep(3)
        # quits the game and closes the client
        return exit()

    # if the user enters "YES" because he/she is ready to play,
    elif ready_to_start == "YES":
        print("Perfect, let's begin. Good luck!")
        time.sleep(3)
        begin_game = True

    # otherwise, if the user enters something other than "YES" or "NO",
    else:
        # proceed anyway with the game
        print("What a weird way to spell YES... ;) Anyway, let's begin!")
        time.sleep(3)
        begin_game = True
