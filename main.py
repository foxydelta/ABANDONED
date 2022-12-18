# CSS 225 Final Project
# Author: Victoria Price
# Date: 12/10/2022

# A program that is the main driver of the game.

import globalvariables
import functions
import startgame
import chapter1
import chapter2
import chapter3
import chapter4
import chapter5


# main method of main.py
def main():

    continue_playing = "YES"

    # initialize the global variables
    globalvariables.init_global_variables()

    # run the start_up function from the startgame module
    startgame.start_up()

    # checks if the player wants to continue playing
    # throughout the game
    while continue_playing.upper() == "YES":
        chapter1.main()
        if globalvariables.ch1_success:
            chapter2.main()
            if globalvariables.ch2_success:
                chapter3.main()
                if globalvariables.ch3_success:
                    chapter4.main()
                    if globalvariables.ch4_success:
                        chapter5.main()
                    else:
                        continue_playing = functions.game_over(4)
                else:
                    continue_playing = functions.game_over(3)
            else:
                continue_playing = functions.game_over(2)
        else:
            continue_playing = "NO"


# run the main method
if __name__ == "__main__":
    main()
