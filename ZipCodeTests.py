import unittest

from ZipCodeItemFile import ZipcodeItem
YELLOW = "\u001b[33m"
GREEN = "\u001b[32m"
MAGENTA = "\u001b[35m"
DEFAULT = "\u001b[0m"

class MyTestCase(unittest.TestCase):
    def test_distance_squared(self):
        z1 = ZipcodeItem(77024, 29.77084, -95.51161, 453, 648)
        z2 = ZipcodeItem(75459, 33.53109, -96.67755, 210, 584)
        pt1 = (300, 400)
        pt2 = (500, 600)
        print(f"{YELLOW}----------------------------- Checking ZipCodeItemFile.py --> distanceSquaredToPoint {DEFAULT}")
        print(f"1) Finding distance squared between {z1} and {pt1}.")
        self.assertAlmostEqual(z1.distance_squared_to_point(pt1), 84913.0, 1)
        print(f"2) Finding distance squared between {z1} and {pt2}.")
        self.assertAlmostEqual(z1.distance_squared_to_point(pt2), 4513.0, 1)
        print(f"3) Finding distance squared between {z2} and {pt1}.")
        self.assertAlmostEqual(z2.distance_squared_to_point(pt1), 41956.0, 1)
        print(f"4) Finding distance squared between {z2} and {pt2}.")
        self.assertAlmostEqual(z2.distance_squared_to_point(pt2), 84356.0, 1)
        print(f"{YELLOW}------------------------------ Done Checking distanceSquaredToPoint. {GREEN}(Passed.){DEFAULT}")

    def test_find_closest_attractor(self):
        z1 = ZipcodeItem(77024, 29.77084, -95.51161, 453, 648)
        z2 = ZipcodeItem(75459, 33.53109, -96.67755, 210, 584)
        att_3 = [(230, 400), (210, 430), (300, 300)]
        att_5 = [(440, 200), (200, 250), (310, 600), (460, 670), (550, 650)]
        print(f"{YELLOW}------------------------------ Checking checking ZipCodeItemFile.py --> findClosestAttractor{DEFAULT}")
        print(f"5) Finding index of closest attractor to {z1} from list {att_3}:")
        self.assertEqual(z1.find_closest_attractor(att_3), 1)
        print(f"6) Finding index of closest attractor to {z2} from list {att_3}:")
        self.assertEqual(z2.find_closest_attractor(att_3), 1)
        print(f"7) Finding index of closest attractor to {z1} from list {att_5}:")
        self.assertEqual(z1.find_closest_attractor(att_5), 3)
        print(f"8) Finding index of closest attractor to {z2} from list {att_5}:")
        self.assertEqual(z2.find_closest_attractor(att_5), 2)
        print(f"{YELLOW}----------------------------- Done checking findClosestAttractor. {GREEN}(Passed.){DEFAULT}")

if __name__ == '__main__':
    unittest.main()
