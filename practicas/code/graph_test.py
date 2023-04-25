from graph import Graph
import unittest


class GraphUnittest(unittest.TestCase):

    def test_initialization(self):

        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        pairs = [
            (1, 2),
            (3, 7),
            (10, 3),
            (1, 10),
            (4, 5),
            (5, 6),
            (8, 9)
        ]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(graph.vertices, vertices)

    def test_exists_path_true(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        pairs = [
            (1, 2),
            (3, 7),
            (10, 3),
            (1, 10),
            (4, 5),
            (5, 6),
            (8, 9),
            (7, 8)
        ]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(graph.exists_path(2, 9), True)

    def test_exists_path_false(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        pairs = [
            (1, 2),
            (3, 7),
            (10, 3),
            (1, 10),
            (4, 5),
            (5, 6),
            (8, 9),
            (7, 8)
        ]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(graph.exists_path(2, 4), False)

if __name__ == "__main__":
    unittest.main()

