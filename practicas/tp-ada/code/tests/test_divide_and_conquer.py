import unittest
from divide_and_conquer.binary_search import binary_search

class DivideAndConquerTests(unittest.TestCase):

    def test_binary_search_inner_true(self):
        self.assertEqual(
            binary_search([1, 3, 5, 12, 77, 1023, 2200], 3),
            True
        )

    def test_binary_search_inner_false(self):
        self.assertEqual(
            binary_search([1, 3, 5, 12, 77, 1023, 2200], 1020),
            False
        )

    def test_binary_search_outer_true(self):
        self.assertEqual(
            binary_search([1, 3, 5, 12, 77, 1023, 2200], 1),
            True
        )

    def test_binary_search_outer_true2(self):
        self.assertEqual(
            binary_search([1, 3, 5, 12, 77, 1023, 2200], 2200),
            True
        )

    def test_binary_search_outer_false(self):
        self.assertEqual(
            binary_search([1, 3, 5, 12, 77, 1023, 2200], -1),
            False
        )

    def test_binary_search_outer_false2(self):
        self.assertEqual(
            binary_search([1, 3, 5, 12, 77, 1023, 2200], 2300),
            False
        )



if __name__ == "__main__":
    unittest.main()