import unittest
from fsa_matcher import fsa_matching

class FSATest(unittest.TestCase):

    def test_middle(self):
        index = fsa_matching("abbbbbbbbababacanaa", "ababaca", "anbc")
        self.assertEqual(index, 9)

    def test_begin(self):
        index = fsa_matching("ababacanaa", "ababaca", "anbc")
        self.assertEqual(index, 0)

    def test_end(self):
        index = fsa_matching("bbbababaca", "ababaca", "anbc")
        self.assertEqual(index, 3)

    def test_inexistent(self):
        index = fsa_matching("bbbababaaca", "ababaca", "anbc")
        self.assertEqual(index, None)


if __name__ == "__main__":
    unittest.main()