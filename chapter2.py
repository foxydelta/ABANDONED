# CSS 225 Final Project
# Author: Victoria Price
# Date: 12/10/2022

# A program that contains the module for Chapter 2.

import time
import globalvariables
import functions
import random


# main method of chapter 2
def main():

    # chapter 2 welcome message
    print("\nWelcome to Chapter 2.")
    time.sleep(3)

    # chapter 2 intro
    print("""
    You wake up early in the morning, having not gotten much 
    sleep. How could you sleep soundly when you've been dumped 
    like trash in a place like this, with absolutely none of 
    the comforts you were once accustomed to? Your tummy rumbles. 
    As a young cat who is still growing, you need nourishment, 
    and you need it fast.
    """)
    time.sleep(5)

    # player options for chapter 2
    print("Here are your choices:"
          "\n 1) dive in dumpsters to find anything edible"
          "\n 2) hunt for mice that have infested the alley"
          "\n 3) claw on the back door of a restaurant, begging for food"
          "\n 0) quit and exit the game")
    time.sleep(3)

    ch2_choice = ""

    # while the player has not chosen to quit,
    while ch2_choice != 0:

        # prompt the player to make a choice
        ch2_choice = input("\nWhat will you do, little kitten? "
                           "Enter the number of the action "
                           "that you want to take: ")

        # player chooses to dive in a dumpster
        if ch2_choice == "1":
            print("""
            You dive into the dumpster, but you can't find anything particularly 
            appetizing. You're starving, so you bite into a bag of trash.
            You nearly choke on the plastic bag, but you're able
            to spit it out.
            """)
            time.sleep(3)
            functions.game_over(2)

        # player chooses to hunt for mice
        elif ch2_choice == "2":
            print("""
            You're a housecat. Or – you were a housecat. You've never 
            had to hunt for your own food before. It was always served 
            to you, warm, delicious, and whenever you wanted it. Now, 
            you're a stray. You don’t know when your next meal will be. 
            You channel your inner carnivore instincts and pounce on an 
            unsuspecting mouse crawling behind a dumpster. You sink your 
            teeth into the rodent and gobble it up. It’s no Fancy Feast, 
            but it'll have to do.
            """)
            time.sleep(5)
            # run the random_event function from the functions module
            # there is a 1/10 chance for the riddle to run after choosing
            # the correct option in chapter 2
            functions.random_event(random.randint(1, 11))
            globalvariables.ch2_success = True
            break

        # player chooses to claw on the back door of a restaurant
        elif ch2_choice == "3":
            print("""
            You claw on the back door of the only restaurant with its lights
            still on and yowl. The owner comes out, kicks you away, and slams
            the door behind him. You're hurt, but you survived the encounter
            and are still hungry.
            """)
            time.sleep(3)
            functions.game_over(2)

        # player chooses to quit the game
        elif ch2_choice == "0":
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
