"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

MIN_RANDOM = 10
MAX_RANDOM = 99
STREAK_TO_WIN = 3

def main():
    streak = 0

    while streak < STREAK_TO_WIN:
        x = random.randint(MIN_RANDOM, MAX_RANDOM)
        y = random.randint(MIN_RANDOM, MAX_RANDOM)

        print("What is {} + {}? ".format(x, y))
        a = input("Your answer: ") 

        if int(a) == x + y:
            streak += 1
            print("Correct! You've gotten " + str(streak) + " in a row.")
        else:
            streak = 0
            print("Incorrect. The expected answer is " + str(x + y))

    print("Congratulation! You mastered addition.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
