# CSS 225 Final Project
# Author: Victoria Price
# Date: 12/10/2022

# A program that contains the module for Chapter 4.

import time
import globalvariables
import functions
import random


# main method of chapter 4
def main():

    # chapter 4 welcome message
    print("\nWelcome to Chapter 4.")
    time.sleep(3)

    # chapter 4 intro
    print("""
    Thank goodness, you’ve made it out of the alley and into the 
    city streets. You know the coyote wouldn't come ever out here 
    where the humans are. Haha! What a coward! Who's the scaredy 
    cat now?! You look around your new surroundings and notice 
    all the happy people walking down the sidewalk, eating on 
    restaurant patios, and shopping at stores. You’ve never seen 
    so many humans in one place. Maybe one of them will have mercy 
    on you? Who will you approach?
    """)
    time.sleep(5)

    # player options for chapter 4
    print("Here are your choices:"
          "\n 1) the little boy and his mother strolling down "
          "the sidewalk with ice cream cones "
          "\n 2) the young mother juggling a toddler on her lap "
          "and two infants in a stroller sitting at the café"
          "\n 3) the tall businessman entering a high-end watch shop"
          "\n 0) quit and exit the game")
    time.sleep(3)

    ch4_choice = ""

    # while the player has not chosen to quit,
    while ch4_choice != 0:

        # prompt the player to make a choice
        ch4_choice = input("\nWhat will you do, little kitten? "
                           "Enter the number of the action "
                           "that you want to take: ")

        # player chooses to approach the little boy and his mother
        if ch4_choice == "1":
            print("""
            You confidently scamper up to the little boy with his 
            mother. You don’t know why you chose them, but you have 
            a gut feeling that they have a lot of love in their 
            hearts. You stop and sit in front of them, giving your 
            most irresistible kitty-cat eyes. The little boy drops 
            his ice cream in awe and runs to grab you. You don’t 
            typically like being held, but he holds you with such 
            care that you actually enjoy it! The mother gasps and 
            kneels down to pet you.
            """)
            time.sleep(5)
            # run the random_event function from the functions module
            # there is a 1/10 chance for the riddle to run after choosing
            # the correct option in chapter 4
            functions.random_event(random.randint(1, 11))
            globalvariables.ch4_success = True
            break

        # player chooses to go up to the young mom with toddlers
        elif ch4_choice == "2":
            print("Oops 4.2")
            time.sleep(3)
            functions.game_over(4)

        # player chooses to go up to the tall businessman
        elif ch4_choice == "3":
            print("Oops 4.3")
            time.sleep(3)
            functions.game_over(4)

        # player chooses to quit and exit the game
        elif ch4_choice == "0":
            print("Sorry to see you go. Please come back soon.")
            time.sleep(3)
            exit(0)
            break

        else:
            print("Invalid option. You should have entered 1, 2, 3, or 0.")
            continue


if __name__ == "__main__":
    main()
