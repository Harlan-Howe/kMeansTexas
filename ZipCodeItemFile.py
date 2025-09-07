import math

from typing import Tuple, List

Coordinates = Tuple[float, float]

class ZipcodeItem:
    """
    This is a class that represents one of the many zip codes in the state of Texas.
    Each zipcode item consists of
    +-----+----------+-----------+---+---+------------------+
    | zip | latitude | longitude | x | y | attractor number |
    +-----+----------+-----------+---+---+------------------+
    """
    def __init__(self,zip, lat, long, x, y):
        self.zip = zip # the number of the zip code (e.g., 77024) - not really used in this program.
        self.lat = lat # the lattitude of this zip code's location -not really used in this program.
        self.long = long # the longitude of this zip code's location - not really used in this program.
        # so, yeah, the rest of this stuff _is_ used.
        self.x = x
        self.y = y
        self.attractor_number = 0

    def distance_squared_to_point(self, pt: Coordinates) -> float:
        """
        calculate the distance squared from this zipcode item to the given coordinates.
        Note that we are finding the square of the distance to save time -- we don't need to square root the answer.
        Note: this point's location is (self.x, self.y)
        :param pt: the coordinates of the point we wish to compare to. This is (pt[0], pt[1]).
        :return: the distance squared.
        """
        # TODO #1: you write this!
        # Hint: this could be as little as one line.

        return -1  # temporary line. Replace this with yours!

    def find_closest_attractor(self, attractor_list: List[Coordinates]) -> int:
        """
        Determines which of the k attractors is closest to this zipcodeitem.
        :param attractor_list: the list of attractors' positions.
        :return: the number (index) of the attractor on the list.
        """
        k = len(attractor_list)
        closest_index = -1
        # TODO #2: You write this one. This should be similar to things you have done before. You're looping through
        #    the attractor_list that was given to you and looking at each attractor's coordinates found there. Identify
        #    the number of the attractor. (e.g., closest_index is 3, the fourth attractor on the list.)
        # hint: make use of self.distanceSquaredToPoint() method you wrote above!



        return closest_index # by the time you get here, closest_index should be the number of the attractor closest
                             # to the given point.


    def __repr__(self) -> str:
        """
        produces a string representation of this zipcodeItem
        :return:
        """
        return f"{self.zip=} @ ({self.x}, {self.y})"