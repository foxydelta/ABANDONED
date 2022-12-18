# CSS 225 Final Project
# Author: Victoria Price
# Date: 12/10/2022

# A program that contains the module for Chapter 3.

import time
import globalvariables
import functions
import random


# main method of chapter 3
def main():

    # chapter 3 welcome message
    print("\nWelcome to Chapter 3.")
    time.sleep(3)

    # chapter 3 intro
    print("""
    After swallowing the mouse up, tail and all, you hear a clank 
    from a metal garbage bin clank. You quickly look behind you to 
    see what made the sound, but all you can see is a big, grey, 
    fluffy tail. Stunned, you stare directly at the garbage bin in 
    utter fear, not sure if you should run. A sly coyote creeps out 
    from behind the bin and smirks at you. What will you do?!
    """)
    time.sleep(5)

    # player options for chapter 3
    print("Here are your choices:"
          "\n 1) hiss at the coyote and try to scare the coyote off"
          "\n 2) defend yourself if the coyote approaches you"
          "\n 3) run down the alley for your life "
          "\n 0) quit and exit the game")
    time.sleep(3)

    ch3_choice = ""

    # while the player has not chosen to quit,
    while ch3_choice != 0:

        # prompt the player to make a choice
        ch3_choice = input("\nWhat will you do, little kitten? "
                           "Enter the number of the action "
                           "that you want to take: ")

        # player chooses to hiss at the coyote
        if ch3_choice == "1":
            print("""
            You hiss at the coyote, but it's clear that he isn't afraid
            of you. He lunges at you, and you barely escape with your life.
            """)
            time.sleep(3)
            functions.game_over(3)

        # player chooses to attempt self-defense
        elif ch3_choice == "2":
            print("""
            You charge at the coyote in self-defense, but he picks you "
            up and throws you across the street. You're hurt, but you can "
            still get away if you try.
            """)
            time.sleep(3)
            functions.game_over(3)

        # player chooses to run down the alley away from the coyote
        elif ch3_choice == "3":
            print("""
            You know that you are no match for that carnivorous canine, 
            and you sprint out of the alley running for your life. 
            Never looking back, this is the only way you can survive 
            this encounter. Although you’re tiny compared to the coyote, 
            you are much faster than him!
            """)
            time.sleep(5)
            # run the random_event function from the functions module
            # there is a 1/10 chance for the riddle to run after choosing
            # the correct option in chapter 3
            functions.random_event(random.randint(1, 11))
            globalvariables.ch3_success = True
            break

        # player chooses to quit the game
        elif ch3_choice == "0":
            print("Sorry to see you go. Please come back soon.")
            time.sleep(3)
            exit(0)
            break

        # player chooses an invalid option
        else:
            print("Invalid option. You should have entered 1, 2, 3, or 0.")
            continue


if __name__ == "__main__":
    main()
