import unittest
from dynamic_programming import longest_increasing_sub_sequence, give_change, exists_k_sum, find_path_weight, find_lcs_length


class DynamicProgrammingTest(unittest.TestCase):

    def test_longest_increasing_sub_sequence(self):
        self.assertEqual(
            longest_increasing_sub_sequence([5, 1, 3, 6, 100, 17, 21]),
            [4, 5, 4, 3, 1, 2, 1]
        )

    def test_give_change(self):
        self.assertEqual(
            give_change(10, [1, 3, 5, 7]),
            2
        )

        self.assertEqual(
            give_change(18, [1, 3, 5, 7]),
            4
        )

    def test_exists_k_sum(self):

        self.assertEqual(
            exists_k_sum(
                5,
                [1]
            ),
            True
        )

        self.assertEqual(
            exists_k_sum(
                17,
                [3, 5]
            ),
            True
        )

    def test_find_path_weight(self):

        weights1 = [
            [1, 2],
            [1, 3]
        ]
        self.assertEqual(find_path_weight(weights1), 5)

        weights2 = [
            [1, 2,  1],
            [1, 5,  3],
            [1, 10, 0]
        ]

        self.assertEqual(find_path_weight(weights2), 7)

        weights3 = [
            [1, 2,  1, 20],
            [1, 5,  3, 10],
            [1, 10, 5, 5 ],
            [6, 6,  7, 1 ]
        ]
        self.assertEqual(find_path_weight(weights3), 18)

    def test_find_lcs_length(self):
        self.assertEqual(find_lcs_length("hola", "bolas"), 3)
        self.assertEqual(find_lcs_length("123", "bolas"), 0)
        self.assertEqual(find_lcs_length("123", "123"), 3)

if __name__ == "__main__":
    unittest.main()