"""Factorial Module"""


class Factorial:
    """Class for solving Factorial"""

    def solve(self, number):
        """Method to solve factorial"""
        # This is the base case
        # If the number is 1, return 1
        # Without this base case. there will be issues.
        if number == 1:
            return number

        # Not the base case, get the answer to the smaller version
        # of the same problem.
        result = self.solve(number - 1)
        # Return the result of the smaller version
        # multiplied with the number.
        # EX: return 5 * 4!
        return number * result
