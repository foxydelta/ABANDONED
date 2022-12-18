# CSS 225 Final Project
# Author: Victoria Price
# Date: 12/10/2022

# A program that contains two functions that are
# used throughout the game, including game_over
# and random_event.

import time


# a function that keeps track of whether or not the player wants to start over
def game_over(chapter):

    # initialize the valid_choice variable to be False
    valid_choice = False

    # while the valid_choice variable holds a False value,
    while not valid_choice:

        # ask the player if they want to play again
        choice = input("Would you like to restart from the beginning of the chapter? "
                       "Type YES or NO: ")

        # if the player enters YES,
        if choice.upper() == "YES":
            # set the valid_choice variable to True
            valid_choice = True

            # if the player is in chapter 1,
            if chapter == 1:
                # import the chapter1 file
                import chapter1
                # call the chapter1 function
                chapter1.main()

            # if the player is in chapter 2,
            elif chapter == 2:
                # import the chapter2 file
                import chapter2
                # call the chapter2 function
                chapter2.main()

            # if the player is in chapter 3,
            elif chapter == 3:
                # import the chapter3 file
                import chapter3
                # call the chapter3 function
                chapter3.main()

            # if the player is in chapter 4,
            elif chapter == 4:
                # import the chapter4 file
                import chapter4
                # call the chapter4 function
                chapter4.main()

            # if the player is in chapter 5,
            elif chapter == 5:
                # import the chapter5 file
                import chapter5
                # call the chapter5 function
                chapter5.main()

            # if the player has completed the game,
            else:
                # congratulate the player
                print("\nCongratulations! You win!")
                time.sleep(3)
                # exit the game
                exit()

        # otherwise, if the player enters NO,
        elif choice.upper() == "NO":
            # set the valid_choice variable to True
            valid_choice = True
            # print a failure message
            print("\nYou fail. Game over.")
            time.sleep(3)
            # exit the game
            exit()


# a function that may randomly ask a riddle to the player in chapters 1 through 4
def random_event(event_chance):

    # if the event_chance randomly picks a 2 from the range 1-10,
    if event_chance == 2:
        print("Something unexpected just happened to you! It's time to solve a riddle.")
        time.sleep(2)
        print("\nI am tall when I am young, and I am short when I am old. What am I?")
        time.sleep(2)
        riddle_answer = input("\nA. a tree"
                              "\nB. a human"
                              "\nC. a candle\n\n")

        if riddle_answer.upper() == "C":
            print("That's correct! Good job. Let's continue.")
            return True

        elif riddle_answer.upper() == "B":
            print("That's incorrect. You suck at riddles... Let's keep playing anyway.")
            return False

        elif riddle_answer.upper() == "A":
            print("That's incorrect. You suck at riddles... Let's keep playing anyway.")
            return False

        else:
            print("Invalid input. You should've entered A, B, or C.")

    # if the event_chance randomly picks a 4 from the range 1-10,
    elif event_chance == 4:
        print("Something unexpected just happened to you! It's time to solve a riddle.")
        time.sleep(2)
        print("\nWhich three numbers give the same result when multiplied and added together?")
        time.sleep(2)
        riddle_answer = input("\nA. 1, 2, 3"
                              "\nB. 2, 4, 6"
                              "\nC. 1, 3, 5\n\n")

        if riddle_answer.upper() == "A":
            print("That's correct! Good job. Let's continue.")
            return True

        elif riddle_answer.upper() == "B":
            print("That's incorrect. You suck at riddles... Let's keep playing anyway.")
            return False

        elif riddle_answer.upper() == "C":
            print("That's incorrect. You suck at riddles... Let's keep playing anyway.")
            return False

        else:
            print("Invalid input. You should've entered A, B, or C.")

    # if the event_chance randomly picks a 6 from the range 1-10,
    elif event_chance == 6:
        print("Something unexpected just happened to you! It's time to solve a riddle.")
        time.sleep(2)
        print("\nWhich creature walks on four legs in the morning two legs in the "
              "afternoon and three legs in the evening?")
        time.sleep(2)
        riddle_answer = input("\nA. a dog"
                              "\nB. a human"
                              "\nC. a chair\n\n")

        if riddle_answer.upper() == "B":
            print("That's correct! Good job. Let's continue.")
            return True

        elif riddle_answer.upper() == "A":
            print("That's incorrect. You suck at riddles... Let's keep playing anyway.")
            return False

        elif riddle_answer.upper() == "C":
            print("That's incorrect. You suck at riddles... Let's keep playing anyway.")
            return False

        else:
            print("Invalid input. You should've entered A, B, or C.")

    # if the event_chance randomly picks an 8 from the range 1-10,
    elif event_chance == 8:
        print("Something unexpected just happened to you! It's time to solve a riddle.")
        time.sleep(2)
        print("\nWhat is 3/7 chicken, 2/3 cat, and 2/4 goat?")
        time.sleep(2)
        riddle_answer = input("\nA. chipmunk"
                              "\nB. chiffon"
                              "\nC. Chicago\n\n")

        if riddle_answer.upper() == "C":
            print("That's correct! Good job. Let's continue.")
            return True

        elif riddle_answer.upper() == "A":
            print("That's incorrect. You suck at riddles... Let's keep playing anyway.")
            return False

        elif riddle_answer.upper() == "B":
            print("That's incorrect. You suck at riddles... Let's keep playing anyway.")
            return False

        else:
            print("Invalid input. You should've entered A, B, or C.")

    # if the event_chance randomly picks a 10 from the range 1-10,
    elif event_chance == 10:
        print("Something unexpected just happened to you! It's time to solve a riddle.")
        time.sleep(2)
        print("\nWhat flies when it's born, lies when it's alive, and runs when it's dead?")
        time.sleep(2)
        riddle_answer = input("\nA. a snowflake"
                              "\nB. an eaglet"
                              "\nC. a fruit fly\n\n")

        if riddle_answer.upper() == "A":
            print("That's correct! Good job. Let's continue.")
            return True

        elif riddle_answer.upper() == "B":
            print("That's incorrect. You suck at riddles... Let's keep playing anyway.")
            return False

        elif riddle_answer.upper() == "C":
            print("That's incorrect. You suck at riddles... Let's keep playing anyway.")
            return False

        else:
            print("Invalid input. You should've entered A, B, or C.")

    # otherwise, if the random generator chose 1, 3, 5, 7, or 9,
    else:
        # do nothing/skip the riddle module for the current chapter
        pass


def main():
    pass


if __name__ == "__main__":
    main()
