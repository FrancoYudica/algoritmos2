import unittest
from divide_and_conquer.binary_search import binary_search
from divide_and_conquer.find_sorted_k import find_sorted_k
from divide_and_conquer.k_sum_subset import exists_k_sum


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

    def test_find_sorted_k(self):
        self.assertEqual(
            find_sorted_k(
                [4, 6, 1, 7, 8, 9, 3, 10],
                3
            ),
            6
        )

    def test_find_sorted_k_first(self):
        self.assertEqual(
            find_sorted_k(
                [4, 6, 1, 7, 8, 9, 3, 10],
                0
            ),
            1
        )

    def test_find_sorted_k_last(self):
        self.assertEqual(
            find_sorted_k(
                [4, 6, 1, 7, 8, 9, 3, 10],
                7
            ),
            10
        )

    def test_find_sorted_k_out_of_range(self):
        self.assertEqual(
            find_sorted_k(
                [4, 6, 1, 7, 8, 9, 3, 10],
                30
            ),
            False
        )
    def test_exists_k_sum(self):
        self.assertEqual(
            exists_k_sum(
                6,
                [1, 2, 4]
            ),
            True
        )

        self.assertEqual(
            exists_k_sum(
                6,
                [1, 2]
            ),
            False
        )

        self.assertEqual(
            exists_k_sum(
                6,
                [6]
            ),
            True
        )

        self.assertEqual(
            exists_k_sum(
                6,
                [6]
            ),
            True
        )

        self.assertEqual(
            exists_k_sum(
                12,
                [1, 4, 6, 5]
            ),
            True
        )
        self.assertEqual(
            exists_k_sum(
                12,
                [1, 4, 6, 0]
            ),
            False
        )
if __name__ == "__main__":
    unittest.main()