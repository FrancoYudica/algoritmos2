from graph import Graph
from graph_utils import *
import unittest


class GraphUnittest(unittest.TestCase):

    def test_initialization(self):

        nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        pairs = [
            (1, 2),
            (3, 7),
            (10, 3),
            (1, 10),
            (4, 5),
            (5, 6),
            (8, 9)
        ]
        graph = Graph.initialize(nodes, pairs)
        self.assertEqual([node.key for node in graph.nodes], nodes)

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
        self.assertEqual(exists_path(graph, 2, 9), True)

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
        self.assertEqual(exists_path(graph, 2, 4), False)

    def test_access(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        graph = Graph.initialize(vertices)
        self.assertEqual(graph[2].key, 2)

    def test_is_connected_false(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        graph = Graph.initialize(vertices)
        self.assertEqual(is_connected(graph), False)

    def test_is_connected_true(self):
        vertices = [1, 2, 3, 4, 5]

        pairs = [
            (1, 5),
            (2, 5),
            (2, 4),
            (4, 5),
            (4, 3)
        ]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(is_connected(graph), True)

    def test_bfs(self):
        vertices = [1, 2, 3, 4, 5]

        # The order of the inserted pairs matters
        pairs = [
            (2, 5),
            (1, 5),
            (2, 4),
            (4, 5),
            (4, 3)
        ]
        graph = Graph.initialize(vertices, pairs)
        bfs_tree = breadth_first_search_tree(graph, 2)

        self.assertEqual(set(bfs_tree.get_adjacent(1)), set([bfs_tree[5]]))
        self.assertEqual(set(bfs_tree.get_adjacent(2)), set([bfs_tree[5], bfs_tree[4]]))
        self.assertEqual(set(bfs_tree.get_adjacent(5)), set([bfs_tree[2], bfs_tree[1]]))
        self.assertEqual(set(bfs_tree.get_adjacent(4)), set([bfs_tree[2], bfs_tree[3]]))
        self.assertEqual(set(bfs_tree.get_adjacent(3)), set([bfs_tree[4]]))

    def test_dfs(self):
        vertices = [1, 2, 3, 4, 5]

        # The order of the inserted pairs matters
        pairs = [
            (1, 5),
            (2, 5),
            (2, 4),
            (4, 5),
            (4, 3)
        ]
        graph = Graph.initialize(vertices, pairs)
        dfs_tree = depth_first_search_tree(graph, 1)
        self.assertEqual(set(dfs_tree.get_adjacent(1)), set([dfs_tree[5]]))
        self.assertEqual(set(dfs_tree.get_adjacent(2)), set([dfs_tree[5], dfs_tree[4]]))
        self.assertEqual(set(dfs_tree.get_adjacent(3)), set([dfs_tree[4]]))
        self.assertEqual(set(dfs_tree.get_adjacent(4)), set([dfs_tree[2], dfs_tree[3]]))
        self.assertEqual(set(dfs_tree.get_adjacent(5)), set([dfs_tree[1], dfs_tree[2]]))


    def test_is_tree(self):
        vertices = [1, 2, 3, 4, 5]

        # The order of the inserted pairs matters
        pairs = [
            (1, 5),
            (2, 5),
            (4, 5),
            (4, 3)
        ]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(is_tree(graph), True)

    def test_is_not_tree(self):
        vertices = [1, 2, 3, 4, 5]

        # The order of the inserted pairs matters
        pairs = [
            (1, 5),
            (2, 5),
            (2, 4),
            (4, 5),
            (4, 3)
        ]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(is_tree(graph), False)

    def test_is_not_complete(self):
        vertices = [1, 2, 3, 4, 5]

        # The order of the inserted pairs matters
        pairs = [
            (1, 5),
            (2, 5),
            (2, 4),
            (4, 5),
            (4, 3)
        ]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(is_complete(graph), False)

    def test_is_complete(self):
        vertices = [1, 2, 3, 4]

        # The order of the inserted pairs matters
        pairs = [
            (1, 2),
            (1, 3),
            (1, 4),

            (2, 3),
            (2, 4),

            (3, 4)
        ]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(is_complete(graph), True)

    def test_convert_tree(self):
        vertices = [1, 2, 3, 4, 5]

        # The order of the inserted pairs matters
        pairs = [
            (1, 5),
            (2, 5),
            (2, 4),
            (4, 5),
            (4, 3),
            (1, 3),
            (1, 4)
        ]
        graph = Graph.initialize(vertices, pairs)

        # Gets the edges that causes cycles
        cycles_pairs = convert_tree(graph)

        # Removes them 
        for (node0, node1) in cycles_pairs:
            graph.remove_dir(node0, node1)

        # Tests if the graph is a tree
        self.assertEqual(is_tree(graph), True)


    def test_connections_count_3(self):
        vertices = [1, 2, 3, 4, 5]

        # The order of the inserted pairs matters
        pairs = [
            (1, 2),
            (3, 4)
        ]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(connections_count(graph), 3)

    def test_connections_count_2(self):
        vertices = [1, 2, 3, 4, 5]

        # The order of the inserted pairs matters
        pairs = [
            (1, 2),
            (1, 3),
            (2, 4)
        ]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(connections_count(graph), 2)

    def test_bes_road_1(self):
        vertices = [1, 2, 3, 4]

        # The order of the inserted pairs matters
        pairs = [(1, 2), (2, 3), (3, 4), (2, 4)]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(set(best_road(graph, 1, 4)), set([graph[1], graph[2], graph[4]]))


    def test_bes_road_2(self):
        vertices = [1, 2, 3, 4]

        # The order of the inserted pairs matters
        pairs = [(1, 2), (2, 3), (3, 4), (2, 4)]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(set(best_road(graph, 1, 2)), set([graph[1], graph[2]]))

    def test_bes_road_3(self):
        vertices = [1, 2, 3, 4]

        # The order of the inserted pairs matters
        pairs = [(1, 2), (2, 3), (3, 4), (2, 4)]
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(set(best_road(graph, 1, 1)), set([graph[1]]))
    

    def test_is_bipartite(self):
        
        vertices = [1, 2, 3, 4, 5, 6]

        pairs = [
            (1, 4), (1, 5), (1, 6),
            (2, 4), (2, 5), (2, 6),
            (3, 4), (3, 5), (3, 6)
        ]

        # The order of the inserted pairs matters
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(is_bipartite(graph), True)


    def test_is_bipartite_false(self):
        
        vertices = [1, 2, 3, 4, 5, 6]

        pairs = [
            (1, 4), (1, 5), (1, 6),
            (2, 4), (2, 5), (2, 6),
            (3, 4), (3, 5), (3, 6),
            (3, 2)                  # This last pair makes it not bipartite
        ]   

        # The order of the inserted pairs matters
        graph = Graph.initialize(vertices, pairs)
        self.assertEqual(is_bipartite(graph), False)
if __name__ == "__main__":
    unittest.main()

