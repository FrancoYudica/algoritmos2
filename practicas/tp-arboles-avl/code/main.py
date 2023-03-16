import unittest
import avl
import binary_tree

class TestAVLTree(unittest.TestCase):

    def test_insert_first_element(self):
        tree = avl.AVLTree()
        insert_value = "Buenas tardes"
        tree.insert(insert_value, 12)
        
        value = tree.access(12)
        self.assertEqual(value, insert_value)

    def test_insert_avl(self):

        keys = [15, 5, 45, 78, 108, 29, 79, 32, 46]
        tree = avl.AVLTree()

        for i, key in enumerate(keys):
            tree.insert(i, key)

        expected = [45, 15, 79, 5, 29, 78, 108, 32, 46]
        result = [node.key for node in avl.traverse_breadth_first(tree)]
        self.assertEqual(expected, result)

    def test_balance_factor_after_insert(self):
        keys = [60, 20, 100, 80, 120, 70, 140, -10]

        tree = avl.AVLTree()
        for i in range(len(keys)):
            tree.insert(str(i), keys[i])

        balance_factors = [node.bf for node in avl.traverse_breadth_first(tree)]
        expected = [1, 1, 0, 1, 0, 0, 0, 0]
        self.assertEqual(balance_factors, expected)

    def test_balance_tree(self):
        nodes = {
            100 : "A",
            90 : "B",
            80 : "C",
            70 : "D",
            60 : "E",
        }

        bt = binary_tree.BinaryTree()

        for key, value in nodes.items():
            bt.insert(value, key)

        tree = avl.AVLTree()
        tree.from_binary_tree(bt)
        expected = ["B", "D", "A", "E", "C"]
        result = [node.value for node in avl.traverse_breadth_first(tree)]
        self.assertEqual(expected, result)

    def test_balance_tree_2(self):
        keys = [15, 5, 45, 78, 108, 29, 79, 32, 46]
        bt = binary_tree.BinaryTree()

        for i, key in enumerate(keys):
            bt.insert(i, key)

        tree = avl.AVLTree()
        tree.from_binary_tree(bt)
        expected = [45, 15, 78, 5, 29, 46, 108, 32, 79]
        result = [node.key for node in avl.traverse_breadth_first(tree)]
        self.assertEqual(expected, result)

    def test_delete_keys(self):
        keys = [60, 20, 100, 80, 120, 10, 110]

        tree = avl.AVLTree()
        for i in range(len(keys)):
            tree.insert(str(i), keys[i])
            
        tree.delete(100)
        result = [node.key for node in avl.traverse_breadth_first(tree)]
        expected = [60, 20, 110, 10, 80, 120]
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)