from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Guide Karel to the newspaper outside and return them to their starting
    position.

    The strategy here is to traverse around the building until a door is
    found. After find the door, Karel will exit and collect the newspaper.
    Karel will then move back inside until they hit a wall. After hitting
    the wall they will traverse around the bulding again until they are
    in the upper left corner.
    """
    
    # find door
    while not top_is_clear() and not beepers_present():
        if front_is_clear():
            move()
        else:
            turn_right()
            move()

    # turn to face out the door
    turn_left()

    # pick up paper
    while not beepers_present():
        move()
        
    pick_beeper()


    # go back inside
    turn_around()
    while front_is_clear():
        move()

    turn_right()

    # traverse inside until in the upper left corner
    while front_is_clear() or not facing_north():
        if front_is_clear():
            move()
        else:
            turn_right()
            move()

    turn_right()


def top_is_clear():
    turn_left()
    clear = front_is_clear()
    turn_right()
    return clear


def turn_around():
    for _ in range(2):
        turn_left()


def turn_right():
    for _ in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
