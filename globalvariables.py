# CSS 225 Final Project
# Author: Victoria Price
# Date: 12/10/2022

# A program that contains the global variables for the game,
# including a class to keep track of the player's name.


# initialize the global variables
def init_global_variables():

    global player_name
    global ch1_success
    global ch1_choice
    global ch2_success
    global ch2_choice
    global ch3_success
    global ch3_choice
    global ch4_success
    global ch4_choice
    global ch5_success
    global ch5_choice

    # default player name: Anonymous
    player_name = "Anonymous"

    # default state of each chapter's success: True
    ch1_success = True
    ch2_success = True
    ch3_success = True
    ch4_success = True
    ch5_success = True

    # default state of each chapter's choices: an empty string
    ch1_choice = ""
    ch2_choice = ""
    ch3_choice = ""
    ch4_choice = ""
    ch5_choice = ""


def player_name():
    return player_name()


def ch1_success():
    return ch1_success()


def ch2_success():
    return ch2_success()


def ch3_success():
    return ch3_success()


def ch4_success():
    return ch4_success()


def ch5_success():
    return ch5_success()


class Player:
    def __init__(self, name):
        self.name = name


def main():
    pass


if __name__ == "__main__":
    main()
