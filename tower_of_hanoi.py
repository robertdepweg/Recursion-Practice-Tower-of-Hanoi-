"""Tower of Hanoi module"""


class TowerOfHanoi:
    """Allows solving the tower of hanoi problem"""

    def solve(self, number_of_discs):
        """Solve the Tower of Hanoi problem"""
        self._move(number_of_discs, "A", "B", "C")

    def _move(self, number, source, temp, destination):
        """Recursive call to solve tower of hanoi"""

        # This is the base case. Nothing to move beyond one disc.
        # So, print the one step out.
        if number == 1:
            print(f"Move disk from tower {source} to tower {destination}")
            # Else, not the base case, so recursively move discs around.
        else:
            # Make a recursive call to move number-1 discs from the
            # source peg to the temp peg.
            self._move(number - 1, source, destination, temp)

            # Move a recursive call to move the 1 sick (bottom) from
            # the source to the destination.
            # This will cause the case case to fire.
            self._move(1, source, temp, destination)

            # Make a recursive call to move number-1 disk from the
            # temp peg to the destination peg.
            self._move(number - 1, temp, source, destination)
