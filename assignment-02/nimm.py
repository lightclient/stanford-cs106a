"""
File: nimm.py
-------------------------
Add your comments here.
"""

INIT_STONES = 20

def main():
    stones = INIT_STONES

    while 0 < stones:
        stones = execute_player_turn(1, stones)
        stones = execute_player_turn(2, stones)


def execute_player_turn(player, stones):
        print_remaining(stones)
        count = query_stone_count(player)
        stones -= count

        if stones <= 0:
            winner = 1 if player != 1 else 2
            print("\nPlayer {} wins!".format(winner))

        print()
        return stones

        
def print_remaining(stones):
    print("There are {} stones left".format(stones))


def query_stone_count(player):
    count = int(input("Player {} would you like to remove 1 or 2 stones? ".format(player)))

    while count != 1 and count != 2:
        count = int(input("Please enter 1 or 2: "))

    return count

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
