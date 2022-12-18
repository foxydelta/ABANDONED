# CSS 225 Final Project
# Author: Victoria Price
# Date: 12/10/2022

# A program that contains the module for Chapter 1.

import random
import time
import globalvariables
import functions


# main method of chapter 1
def main():

    # chapter 1 welcome message
    print("\nWelcome to Chapter 1.")
    time.sleep(3)

    # chapter 1 intro
    print("""
    You watch in horror as the human you thought would always take
    care of you and love you drives off into the distance. It's a
    cold, dark autumn night, and the only thing you can see is what's
    illuminated by flickering streetlights in this gloomy alley.
    """)
    time.sleep(5)

    # player options for chapter 1
    print("Here are your choices:"
          "\n 1) chase after your owner's car"
          "\n 2) cry for help, hoping someone will rescue you"
          "\n 3) find a safe space to rest for the night"
          "\n 0) quit and exit the game")
    time.sleep(3)

    ch1_choice = ""

    # while the player has not chosen to quit,
    while ch1_choice != 0:

        # ask the player to choose an option
        ch1_choice = input("\nWhat will you do, little kitten? "
                           "Enter the number of the action "
                           "that you want to take: ")

        # player chooses to chase after owner's car
        if ch1_choice == "1":
            print("""
            You run as fast you can to try to chase after your owner's 
            car, but you just too slow. They left you here, and they're 
            not coming back for you.
            """)
            time.sleep(3)
            functions.game_over(1)

        # player chooses to cry for help
        elif ch1_choice == "2":
            print("""
            You cry for help, but no one hears you. You are all alone,
            and you are afraid. No one is coming to save you.
            """)
            time.sleep(3)
            # call game over function for chapter 1
            functions.game_over(1)

        # player chooses to find a safe space to rest
        elif ch1_choice == "3":
            print("""
            As if this night couldn't get any worse, it begins 
            to rain. It’s as if the sky is crying because of your 
            misfortune. There’s nothing a cat hates more than being 
            wet – so you rush to find somewhere to shield you from 
            the rain. You manage to find a dry spot where a small 
            shed has been set up, and squeeze through the door. 
            It’s warmer much in here than it is outside. Your eyes 
            get heavy as the downpour lulls you to sleep.
            """)
            time.sleep(5)
            # run the random_event function from the functions module
            # there is a 1/10 chance for the riddle to run after choosing
            # the correct option in chapter 1
            functions.random_event(random.randint(1, 11))
            # set the chapter 1 success flag to True
            globalvariables.ch1_success = True
            break

        # player chooses to quit the game
        elif ch1_choice == "0":
            print("Sorry to see you go. Please come back soon.")
            time.sleep(3)
            exit(0)
            break

        # player enters an invalid option
        else:
            print("Invalid option. You should have entered 1, 2, 3, or 0.")
            continue


if __name__ == "__main__":
    main()
