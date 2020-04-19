from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    Draw a checkerboard with beepers.

    The strategy Karel uses is to construct each row and return to their
    starting position for the row before determining if they can continue to
    a higher row. If a beeper is in the first position in the row, Karel will
    move forward once to offset the next row -- thereby creating the checkered
    pattern.
    """

    turn_left()

    while front_is_clear():
        turn_right()

        place_checkers()
        turn_around()

        while front_is_clear():
            move()

        turn_around()

        # make sure to offset checkers
        if beepers_present():
            move()

        turn_left()
        move()

    # place checkers on top row
    turn_right()
    place_checkers()


def place_checkers():
    put_beeper()

    while front_is_clear():
        move()

        if front_is_clear():
            move()
            put_beeper()


def turn_right():
    for _ in range(3):
        turn_left()


def turn_around():
    for _ in range(2):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
