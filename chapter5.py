# CSS 225 Final Project
# Author: Victoria Price
# Date: 12/10/2022

# A program that contains the module for Chapter 5.

import time
import globalvariables


# main method of chapter 5
def main():

    # chapter 5 welcome message
    print("\nWelcome to Chapter 5.")
    time.sleep(3)

    # chapter 5 intro
    print("""
    The mother takes you from her son and says, “Oh my gosh, what 
    are you doing all by yourself? You’re so dirty, you poor 
    thing… Let’s take you home and get you cleaned up.” Her son 
    squeals with glee as his mother carries you back to their 
    family car. “I love that kitty! Mommy, I always wanted a kitty!” 
    She smiles and tears fall down her face as she realizes that 
    she just saved your life. After the car ride home, the mother 
    puts you down on the ground so that she can open the front 
    door with her keys.
    """)
    time.sleep(5)

    # player options for chapter 5
    print("Here are your choices:"
          "\n 1) run away from them, but try to find someone else "
          "to take you home"
          "\n 2) flee from them, realizing you don’t want to be a pet anymore"
          "\n 3) snuggle up next to the mother and her son’s legs and purr"
          "\n 0) quit and exit the game")
    time.sleep(1)

    ch5_choice = ""

    while ch5_choice != 0:

        # player is prompted to make a choice
        ch5_choice = input("\nWhat will you do, little kitten? "
                           "Enter the number of the action "
                           "that you want to take: ")

        # player chooses to run away from the mother and her son
        if ch5_choice == "1":
            print("""
            You realize that you just don't want to be their pet. You
            don't picture yourself living in this house with this family.
            You want someone else to take care of you. Someone more
            responsible. You try to return to the street where
            you were found, but you can't find your way back.
            You're lost. There's no one else around.
            It's back to the stray life for you...
            """)
            time.sleep(3)
            print(f"GAME OVER - Thanks for playing, {globalvariables.player_name}!")
            time.sleep(1)
            exit(0)
            break

        # player chooses to flee and become a permanent stray
        elif ch5_choice == "2":
            print("""
            You're just not cut out to be a pet. You're a stray at heart.
            The taste of stray life got your blood pumping, and you want more of it.
            You run away from the mother and her son, never looking back.
            The streets are your home now.
            """)
            time.sleep(3)
            print(f"GAME OVER - Thanks for playing, {globalvariables.player_name}!")
            time.sleep(1)
            exit(0)
            break

        # player chooses to snuggle up to the little boy
        elif ch5_choice == "3":  # happy ending
            print("""
            "Awwww, what a good kitty. I can’t believe someone tried 
            to get rid of you," says the mother. "We will never get 
            rid of you, kitty cat, right mama?" adds the boy. 
            "Of course not, sweetie. This little cat is a part of our 
            family now,” she responds. You feel your heart race and 
            your eyes start to water. So this is what it feels like 
            to be loved!
            """)
            time.sleep(5)
            globalvariables.ch5_success = True
            print(f"GAME OVER - Thanks for playing, {globalvariables.player_name}!")
            time.sleep(1)
            exit(0)
            break

        # player chooses to quit and exit the game
        elif ch5_choice == "0":
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
