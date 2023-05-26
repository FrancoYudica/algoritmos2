import unittest
from backtracking import give_change, maximize_bag_weight, longest_sub_sequence, sum_subset

class BacktrackingTest(unittest.TestCase):

    def test_give_change(self):
        self.assertEqual(give_change(14, [1, 2, 6, 8, 10]), [8, 6])
        self.assertEqual(give_change(20, [1, 3, 11, 7, 12]), [12, 7, 1])

    def test_bag(self):
        self.assertEqual(maximize_bag_weight(22, [30, 17, 7, 8, 9, 6]), [9, 7, 6])
        self.assertEqual(maximize_bag_weight(22, [30, 17, 8, 9, 6]), [17])

    def test_longest_sub_sequence(self):
        self.assertEqual(longest_sub_sequence([5, 1, 3, 6, 100, 17, 21]), [1, 3, 6, 17, 21])

    def test_sum_subset(self):
        self.assertEqual(sum_subset(14, [10, 4]), True)
        self.assertEqual(sum_subset(14, [10, 3]), False)
        self.assertEqual(sum_subset(15, [8, 6, 7, 5, 3, 10, 9]), True)
        self.assertEqual(sum_subset(15, [11, 6, 5, 1, 7, 13, 12]), False)


if __name__ == "__main__":
    unittest.main()