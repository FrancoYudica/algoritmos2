import unittest


from greedy.administrate_tasks import administrate_tasks, Task
from greedy.find_pairs import find_pairs
from greedy.maximize_bag import maximize_bag, Can


class DynamicProgrammingTest(unittest.TestCase):

    def test_administrate_1(self):
        tasks = [
            Task("T1", 0, 2),
            Task("T2", 1, 4),
            Task("T3", 3, 1),
            Task("T4", 5, 2),
            Task("T5", 6, 2),
            Task("T6", 8, 6),
            Task("T7", 15, 2),
            Task("T8", 16, 2),
            Task("T9", 19, 2)
        ]
        start = 0
        end = 21

        selected = administrate_tasks(tasks, start, end)
        self.assertEqual(selected, ["T1", "T3", "T4", "T6", "T7", "T9"])

    def test_administrate_cut_end_time(self):
        tasks = [
            Task("T1", 0, 2),
            Task("T2", 1, 4),
            Task("T3", 3, 1),
            Task("T4", 5, 2),
            Task("T5", 6, 2),
            Task("T6", 8, 6),
            Task("T7", 15, 2),
            Task("T8", 16, 2),
            Task("T9", 19, 2)
        ]
        start = 0
        end = 16

        selected = administrate_tasks(tasks, start, end)
        self.assertEqual(selected, ["T1", "T3", "T4", "T6"])

    def test_administrate_cut_start_time(self):
        tasks = [
            Task("T1", 0, 2),
            Task("T2", 1, 4),
            Task("T3", 3, 1),
            Task("T4", 5, 2),
            Task("T5", 6, 2),
            Task("T6", 8, 6),
            Task("T7", 15, 2),
            Task("T8", 16, 2),
            Task("T9", 19, 2)
        ]
        start = 1
        end = 21

        selected = administrate_tasks(tasks, start, end)
        self.assertEqual(selected, ["T2", "T4", "T6", "T7", "T9"])


    def test_find_pairs(self):
        numbers = [5, 8, 1, 4, 7, 9]
        self.assertEqual(find_pairs(numbers), 12)

    def test_maximize_bag(self):
        cans = [
            Can("C1", 10, 0.4),
            Can("C2", 9,  1.4),
            Can("C3", 11, 0.4),
            Can("C4", 10, 4.4),
            Can("C5", 14, 3.4),
            Can("C6", 3, 3.5)
        ]
        max_weight = 30
        self.assertEqual(["C4", "C6", "C5"], maximize_bag(cans, max_weight))

if __name__ == "__main__":
    unittest.main()