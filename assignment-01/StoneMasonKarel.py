from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    Repairs broken columns in the quad.

    The strategy here is to repair columns by moving north until the front is
    blocked. At each position, Karel will check to see if a beeper is present.
    If it isn't, Karel will place one to repair the column. After reaching the
    top of the column, Karel will return to floor and move on to the next
    column.
    """

    # in the case of a 1 x N world, where `front_is_blocked()` returns true,
    # karel should still repair the single column
    turn_left()
    repair_column()

    while front_is_clear():
        move_to_next_column()
        turn_left()
        repair_column()


def repair_column():
    """
    Repair a column of arbitary height. It is assumed that Karel will already be
    facing North.
    """

    while front_is_clear():
        repair()
        move()
    repair()

    turn_around()

    while front_is_clear():
        move()

    turn_left()


def repair():
    if beepers_present():
        pass
    else:
        put_beeper()


def move_to_next_column():
    for _ in range(4):
        move()


def turn_around():
    for _ in range(2):
        turn_left()


def turn_right():
    for _ in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
