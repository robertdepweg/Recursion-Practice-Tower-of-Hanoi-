"""Program code"""

# First party imports
from factorial import Factorial


def main(*args):
    """Method to run program"""

    # Create insiance opf Factorial class to use
    factorial = Factorial()

    # Show menu and collect input
    print("Enter 1 for factorial, 2 for Tower of Hanoi, 3 to exit.")
    choice = input()

    # While choice is less than exit criteria.
    # NOTE: Assuming good input from user.
    while int(choice) < 3:
        # If solving factorial
        if choice == "1":
            # Do factorial
            print("What number would you like to solve? 5 is a good choice.")
            print("> ", end="")
            number = int(input())

            print()
            print(f"solving {number}!")
            print("The answer is: ", end="")
            print(factorial.solve(number))

        elif choice == "2":
            # Do Tower of Hanoi
            pass

        # Re-show menu and collect input
        print()
        print()
        print("Enter 1 for factorial, 2 for Tower of Hanoi, 3 to exit.")
        choice = input()
