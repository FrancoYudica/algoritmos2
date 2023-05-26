import unittest
from dynamic_programming import longest_sub_sequence

class DynamicProgrammingTest(unittest.TestCase):

    def test_longest_sub_sequence(self):
        self.assertEqual(
            longest_sub_sequence([5, 1, 3, 6, 100, 17, 21]),
            [4, 5, 4, 3, 1, 2, 1]
        )

if __name__ == "__main__":
    unittest.main()