"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    print("This program subtracts one number from another")
    first = input("Enter first number: ")
    second = input("Enter second number: ")
    print("The result is " + str(float(first) - float(second)))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
