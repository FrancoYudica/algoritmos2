import unittest
from binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        pass

    def test_insert_first_element(self):
        """ Insertar un solo elemento en un arbol vacio y verificar su valor
        """
        bt = BinaryTree()
        bt.insert("comienzo", 1)
        self.assertEqual(bt.access(bt, bt.root.key), "comienzo")

    def test_insert_element_check_order(self):
        """ Insertar un elemento en un arbol y verificar su posicion
        """
        strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

        keys = [10, 5, 20, 8, 13, 18, 22, 2, 9, 40, 21, 11, 7, 3, 1]
        bt = BinaryTree()
        for a in range(0, 15):
            bt.insert(strings[a], keys[a])

        self.assertEqual(bt.access(bt.root.rightnode.rightnode.leftnode.key), "b")

    def test_delete_leaf_check_order(self):
        """ Borrar una rama de un arbol y verificar la posicion del elemento eliminado
        """
        strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        keys = [10, 5, 20, 8, 13, 22]
        bt = BinaryTree()
        for a in range(0, 6):
            bt.insert(strings[a], keys[a])
        bt.delete('2')
        self.assertEqual(bt.root.leftnode.key, 8)

    def test_delete_element(self):
        """ Borrar una hoja de un arbol y verificar la posicion inexistente
        """
        strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        keys = [10, 5, 20, 8, 13, 22]
        bt = BinaryTree()
        for a in range(0, 6):
            bt.insert(strings[a], keys[a])
        bt.delete("5")
        res = bt.search('5')
        self.assertEqual(res, None)

    def test_delete_inexistent_element(self):
        """ Borrar una hoja inexistente de un arbol y verificar el error
        """
        strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        keys = [10, 5, 20, 8, 13, 22]
        bt = BinaryTree()
        for a in range(0, 6):
            bt.insert(strings[a], keys[a])
        res = bt.delete(54)
        self.assertEqual(res, None)

    def test_delete_root(self):
        """ Borrar el root de un arbol y verificar el nuevo root
        """
        strings = ["uno", "dos", "tres", "cuatro", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        keys = [10, 5, 20, 18]
        bt = BinaryTree()
        for a in range(0, 3):
            bt.insert(strings[a], keys[a])
            
        # print()
        # print()
        # print("root key:",bt.root.key,", value:",bt.root.value)
        # print("Elimino el root: 10 - uno")
        bt.delete("uno")
        # print("nuevo root key:",bt.root.key, ", value:",bt.root.value)
        res = bt.root.value
        # print()
        # print()
        self.assertEqual(res, "tres")

    def test_search(self):
        """ Busqueda de un elemento en un arbol y verificar su posicion y contenido
        """
        strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        keys = [10, 5, 20, 8, 13, 18, 22, 2, 9, 40, 21, 11, 7, 3, 1]
        bt = BinaryTree()
        for a in range(0, 15):
            bt.insert(strings[a], keys[a])
        res = bt.search("7")
        self.assertEqual(res, 22)

    def test_search_inexistent(self):
        """ Busqueda de un elemento inexistente en un arbol y verificar None
        """
        strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

        keys = [10, 5, 20, 8, 13, 18, 22, 2, 9, 40, 21, 11, 7, 3, 1]
        bt = BinaryTree()
        for a in range(0, 15):
            bt.insert(strings[a], keys[a])
        res = bt.search("g")
        self.assertEqual(res, None)

    def test_access_inexistent_element(self):
        """ Acceder un elemento inexistente un arbol y verificar el error
        """
        strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        keys = [10, 5, 20, 8, 13, 22]
        bt = BinaryTree()
        for a in range(0, 6):
            bt.insert(strings[a], keys[a])
        res = bt.access(55)
        self.assertEqual(res, None)

    def test_insert_first_element(self):
        """ Insertar un solo elemento en un arbol vacio y verificar su valor
        """
        bt = BinaryTree()
        bt.insert('comienzo', 1)
        self.assertEqual(bt.access(bt.root.key), "comienzo")


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)


