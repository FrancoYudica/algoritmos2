import unittest
from kmp_matcher import kmp_matcher

class KMPTest(unittest.TestCase):

    def test_middle(self):
        index = kmp_matcher("abbbbbbbbababacanaa", "ababaca")
        self.assertEqual(index, 9)

    def test_begin(self):
        index = kmp_matcher("ababacanaa", "ababaca")
        self.assertEqual(index, 0)

    def test_end(self):
        index = kmp_matcher("bbbababaca", "ababaca")
        self.assertEqual(index, 3)

    def test_inexistent(self):
        index = kmp_matcher("bbbababaaca", "ababaca")
        self.assertEqual(index, None)


if __name__ == "__main__":
    unittest.main()