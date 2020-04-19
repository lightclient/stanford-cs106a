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

    Since there is no way to count the number of moves Karel makes, Karel uses
    y-axis to record how far they've moved. Karel starts the world moving
    forward one and up one until they reach the far East wall. Karel then turns
    around and move forward one and down two. This is equivalent to counting
    the number of spaces in the world and dividing by two.
    """
    
    while front_is_clear():
        move_forward_and_up()

    turn_right()

    while front_is_clear():
        move_forward_and_down_two()

    turn_right()
    put_beeper()


def move_forward_and_up():
    move()
    turn_left()
    move()
    turn_right()

def move_forward_and_down_two():
    turn_right()
    move()
    turn_left()
    move()

    if front_is_clear():
        move()


def turn_right():
    for _ in range(3):
        turn_left()

def turn_around():
    for _ in range(2):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
