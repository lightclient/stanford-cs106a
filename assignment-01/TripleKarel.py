from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    Paint the exterior of three buildings.

    The strategy here is to face Karel towards the building at the beginning of
    each iteration so that they can determine if they are still against the
    building. Given the layout of the worlds, three sides of each building are
    painted. This is reflected in the implementation of `paint_building`.
    """

    # adjust to face karel directly towards building 1 
    turn_left()

    paint_building()
    paint_building()
    paint_building()


def paint_building():
    """
    Paints three sides of an individual building. It assumes that before called,
    Karel is facing the building directly.
    """
    paint_side()
    move_around_corner()

    paint_side()
    move_around_corner()
    
    paint_side()

    # given the expected layout, karel will always end up at facing the next
    # building with their feet, so we should turn them right so that they are
    # facing it head on.
    turn_right()


def move_around_corner():
    move()
    turn_left()


def paint_side():
    while front_is_blocked():
        put_beeper()
        turn_right()
        move()
        turn_left()


def turn_right():
    for _ in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
