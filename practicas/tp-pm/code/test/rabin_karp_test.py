import unittest
from rabin_karp import rabin_karp

class RabinKarpTest(unittest.TestCase):

    def test_middle(self):
        index = rabin_karp("abbbbbbbbababacanaa", "ababaca")
        self.assertEqual(index, 9)

    def test_begin(self):
        index = rabin_karp("ababacanaa", "ababaca")
        self.assertEqual(index, 0)

    def test_end(self):
        index = rabin_karp("bbbababaca", "ababaca")
        self.assertEqual(index, 3)

    def test_inexistent(self):
        index = rabin_karp("bbbababaaca", "ababaca")
        self.assertEqual(index, None)


if __name__ == "__main__":
    unittest.main()