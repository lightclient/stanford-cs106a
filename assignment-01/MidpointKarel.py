from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Find the midpoint of the world. 

    The strategy here is to have two markers on either end of the world and 
    slowly move them closer to the center. Karel will know that the midpoint
    has been found when they place a marker adjacent to the other marker.
    """
    put_beeper()

    # in the case of  a 1 x 1 world, karel should simply flip upside down as
    # midpoint is also equal to the starting position
    if front_is_blocked():
        turn_around()
    else:
        while front_is_clear():
            move()

        turn_around()

        while no_beepers_present():
            put_beeper()
            move()

            while no_beepers_present():
                move()

            pick_beeper()
            turn_around()
            move()

        if facing_east():
            turn_around()


def turn_around():
    for _ in range(2):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
