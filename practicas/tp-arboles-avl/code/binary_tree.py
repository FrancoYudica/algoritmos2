
class BinaryNode:
    key = None
    value = None
    leftnode = None
    rightnode = None
    parent = None

    def __str__(self):
        return f"key:{self.key}, value:{str(self.value)}"
    

class BinaryTree:

    def __init__(self):
        self.root = None


    def search(self, value):
        """
        Implementación del algoritmo de búsqueda en un arbol binario de búsqueda.
        Si el árbol binario está balanceado la complejidad del algoritmo es O(log(n))
        Pero si no está balanceado, puede ser que los nodos esten conectados en forma de lista
        en el peor de los casos, por lo tanto la complejidad es O(n)
        :param tree: Arbol binario de búsqueda
        :param value: Valor a buscar
        :return: Key del nodo con el valor, puede ser None
        """
        node = self._serach_recursive(value, self.root)
        if node is None:
            return None
        return node.key

    def access(self, key):
        """
        Implementación del algoritmo de access en un árbol binario de búsqueda.
        Si el árbol está balanceado, la complejidad de insert es de O(log(n))
        Pero, si no lo está, en el peor de los casos esta puede ser O(n)
        :param tree: arbol binario de búsqueda
        :param key: key del nodo a buscar
        :return: valor del nodo con dicha key
        """
        node = self._access_recursive(self.root, key)
        if node is None:
            return None
        return node.value


    def update(self, key, value):
        """
        Implementación del algoritmo de update en un árbol binario de búsqueda.
        Nótese que utliza a la función _access_node, función interna de access,
        para acceder al nodo dada una key. Si es que se encuentra el nodo, se
        modifica su valor. Por lo tanto, update tiene la misma complejidad que
        access
        :param tree: arbol binario de búsqueda
        :param value: Nuevo valor del nodo a encontrar
        :param key: Key del nodo buscado
        :return: Key del nodo encontrado, de otro modo None
        """

        node = self._access_recursive(self.root, key)
        if node is None:
            return None
        
        node.value = value
        return key


    def delete_key(self, key):
        node = self._access_recursive(self.root, key)
        if node is None:
            return False
        
        self._delete_recursive(node)
        return True


    def delete(self, value):
        """
        Implementación del algoritmo de delete en un árbol binario de búsqueda
        Nótese que la complejidad de delete en el peor de los casos es O(n),
        dado que utiliza la función access y además la búsqueda del menor nodo
        return: key del nodo eliminado, o None
        """
        node = self._serach_recursive(value, self.root)
        if node is None:
            return 
        
        self._delete_recursive(node)
        return node.key

    def height(self):
        return self._height(self.root)

    def _height(self, node):

        if node is None:
            return 0

        return 1 + max(self._height(node.leftnode), self._height(node.rightnode))


    def _delete_recursive(self, node):
        
        # 1) Dos sub-árboles
        if node.leftnode is not None and node.rightnode is not None:
            # Busco el nodo mas chico dentro del sub-árbol derecho
            smallest = node.rightnode
            while smallest.leftnode is not None:
                smallest = smallest.leftnode

            # Llegado a este punto, le copio los valores en node, pues este es el
            # sucesor de node
            node.key = smallest.key
            node.value = smallest.value

            # Pero debo eliminar el nodo
            self._delete_recursive(smallest)
            return
        
        # 2) Cuando solo tiene un sub-árbol izquierdo
        if node.leftnode is not None:

            # Establece las referencias entre el sub nodo izquierdo
            # y el parent
            parent = node.parent
            sucessor = node.leftnode

            if parent is None:
                self.root = sucessor
                return

            sucessor.parent = parent

            if parent.leftnode == node:
                parent.leftnode = sucessor
            else:
                parent.rightnode = sucessor

            # Desconecta al nodo
            node.parent = None
            node.leftnode = None
            return
        
        # 3) Cuadno solo tiene un sub-árbol derecho
        if node.rightnode is not None:
            parent = node.parent
            sucessor = node.rightnode

            if parent is None:
                self.root = sucessor
                return

            sucessor.parent = parent

            if parent.leftnode == node:
                parent.leftnode = sucessor
            else:
                parent.rightnode = sucessor

            # Desconecta al nodo
            node.parent = None
            node.leftnode = None
            return

        # 4) En este caso, el nodo no tiene ningún hijo
        # Es tan fácil como eliminar las referncias entre el parent y el nodo
        parent = node.parent

        if parent is None:
            self.root = None
            return

        if parent.leftnode == node:
            parent.leftnode = None
        else:
            parent.rightnode = None
        node.parent = None

    def insert(self, value, key):
        """
        Implementación del algoritmo de inserción en un árbol binario de búsqueda.
        Si el árbol está balanceado, la complejidad de insert es de O(log(n))
        Pero, si no lo está, en el peor de los casos esta puede ser O(n)
        :param tree: Árbol binario de búsqueda
        :param value: Valor del nodo a insertar en el ábrol
        :param key: Key del nodo a insertar en el árbol
        :return: None
        """

        node = BinaryNode()
        node.key = key
        node.value = value
        if self.root is None:
            self.root = node
        else:
            self._insert_recursive(self.root, node)
            
    def _serach_recursive(self, value, currentNode):
        """
        Busca el valor en todos los nodos del árbol, O(n) en el peor caso
        """
        if currentNode is None:
            return None
        
        if currentNode.value == value:
            return currentNode
        
        if currentNode.leftnode is not None:
            found = self._serach_recursive(value, currentNode.leftnode)

            if found is not None:
                return found
            
        if currentNode.rightnode is not None:
            found = self._serach_recursive(value, currentNode.rightnode)

            if found is not None:
                return found
            
    def _insert_recursive(self, current, node):
        """
        Inserción en arbol binario de búsqueda
        """
        if current.key < node.key:
            if current.rightnode is None:
                current.rightnode = node
                node.parent = current
                return

            self._insert_recursive(current.rightnode, node)

        else:
            if current.leftnode is None:
                current.leftnode = node
                node.parent = current
                return

            self._insert_recursive(current.leftnode, node)

    def _access_recursive(self, current, key):
        if current is None:
            return 
        
        if current.key == key:
            return current
        
        if current.key < key:
            return self._access_recursive(current.rightnode, key)
        
        return self._access_recursive(current.leftnode, key)
    