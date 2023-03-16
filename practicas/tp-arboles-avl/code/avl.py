

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None
    height = 0

    def __repr__(self) -> str:
        return f"(key={self.key}: val={self.value}, bf={self.bf}, height={self.height})"

class AVLTree:

    def __init__(self) -> None:
        self.root = None

    def insert(self, value, key):

        # Creo el nodo a insertar
        node = AVLNode()
        node.key = key
        node.value = value
        node.bf = 0
        node.height = 0

        # Inserto el nodo
        if self.root is None:
            self.root = node

        else:
            self._insert_bst(self.root, node)

        self._update_bf(node)

    def access(self, key):
        node = self._access_bst(self.root, key)
        if node is None:
            return None
        return node.value

    def _insert_bst(self, currentNode, node):
        """
        Inserción en arbol binario de búsqueda
        """
        if currentNode.key < node.key:
            if currentNode.rightnode is None:
                currentNode.rightnode = node
                node.parent = currentNode
                return

            self._insert_bst(currentNode.rightnode, node)

        else:
            if currentNode.leftnode is None:
                currentNode.leftnode = node
                node.parent = currentNode
                return

            self._insert_bst(currentNode.leftnode, node)
    

    def _update_node(self, node):
        """
        Calcula la altura del nodo basándose en las alturas de los nodos hijos
        Y luego calcula balance factor
        Nótese que se inicializan las alturas de los hijos con -1, de tal forna
        que si no tiene hijos la diferencia da 0 (bf) y luego, la altura del
        nodo también sera 0
        """
        left_height = -1
        right_height = -1

        if node.leftnode is not None:
            left_height = node.leftnode.height
        if node.rightnode is not None:
            right_height = node.rightnode.height

        node.height = 1 + max(left_height, right_height)
        node.bf = left_height - right_height

    def _update_bf(self, current):

        if current is None:
            return
        
        self._update_node(current)

        # Found the unbalanced node, re balance the node and quits recursion
        if abs(current.bf) > 1:
            self._balance_node(current)
            return
            #En este caso no retorno, pues necesito calcular los
            # balance factor de todos los nodos hacia arriba

        self._update_bf(current.parent)

    def _access_bst(self, current, key):
        if current is None:
            return 

        if current.key == key:
            return current

        if current.key < key:
            return self._access_bst(current.rightnode, key)
        
        return self._access_bst(current.leftnode, key)

    def balance(self):

        """
        Si el AVL tiene desbalances, por haberse copiado de un bst,
        se utiliza balance. 
        Luego de llamar al método balance, el árbol resulta ser un AVL balanceado
        """

        def _balance_node_upwards(node):
            """
            Parte desde las hojas hasta llegar hasta la raíz, por eso es upwards
            El objetivo es balancear los sub-árboles mas chicos hasta llegar a la raíz,
            de esta manera el problema se simplifica y siempre sabemos que los sub-árboles
            izquierdos y derechos se encuentran balanceados
            """
            if node is None:
                return
            
            # Primero bajamos hasta llegar a las hojas
            _balance_node_upwards(node.rightnode)
            _balance_node_upwards(node.leftnode)

            # Si este fuera el primer nodo, la altura sería 0 ya que la altura de los
            # nodos está inicializada en 0. Es por eso que no hace falta hacer un caso
            # especial para los nodos hoja
            self._update_node(node)

            # Si se encuentra desbalanceado
            if abs(node.bf) > 1:

                # Balanceamos el nodo
                self._balance_node(node)
                
                # Continúo con el proceso hasta llegar hasta la raíz
                _balance_node_upwards(node.parent)

        _balance_node_upwards(self.root)


    def delete(self, key):
        node = self._access_bst(self.root, key)
        if node is None:
            return False

        # Keeps track of the parent        
        parent = node.parent

        # Removes the node fron the tree
        sucessor = self._delete_recursive_bst(node)

        # Actualiza balance factors y balancea 
        # en caso de ser necesario desde el sucesor
        if sucessor is not None:
            self._update_bf(sucessor)

        # En caso de no tener sucesor, parte desde
        # el parent
        elif parent is not None:
            self._update_bf(parent)

    
    def _delete_recursive_bst(self, node):
        """
        Delete usado en BinaryTree
        """

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
            return self._delete_recursive_bst(smallest)
        
        # 2) Cuando solo tiene un sub-árbol izquierdo
        if node.leftnode is not None:

            # Establece las referencias entre el sub nodo izquierdo
            # y el parent
            parent = node.parent
            sucessor = node.leftnode

            if parent is None:
                self.root = sucessor
                return sucessor

            sucessor.parent = parent

            if parent.leftnode == node:
                parent.leftnode = sucessor
            else:
                parent.rightnode = sucessor

            # Desconecta al nodo
            node.parent = None
            node.leftnode = None
            return sucessor
        
        # 3) Cuadno solo tiene un sub-árbol derecho
        if node.rightnode is not None:
            parent = node.parent
            sucessor = node.rightnode

            if parent is None:
                self.root = sucessor
                return sucessor

            sucessor.parent = parent

            if parent.leftnode == node:
                parent.leftnode = sucessor
            else:
                parent.rightnode = sucessor

            # Desconecta al nodo
            node.parent = None
            node.leftnode = None
            return sucessor

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

    def from_binary_tree(self, bt):
        """
        Lo que hace esta función, es dado un binary tree, copiar
        todos sus valores en este arbol.
        Nótese que la copia inicial no mantiene las propiedades
        del AVL
        """
        def _copy_node_recursive(current_bt):
            """
            Funcion recursiva encargada de copiar las key y value
            de los nodos del otro arbol binario en el AVL
            """
            if current_bt is None:
                return

            avlNode = AVLNode()
            avlNode.key = current_bt.key
            avlNode.value = current_bt.value

            avlNode.leftnode = _copy_node_recursive(current_bt.leftnode)

            if avlNode.leftnode is not None:
                avlNode.leftnode.parent = avlNode

            avlNode.rightnode = _copy_node_recursive(current_bt.rightnode)

            if avlNode.rightnode is not None:
                avlNode.rightnode.parent = avlNode
            return avlNode
        
        self.root = _copy_node_recursive(bt.root)
        self.balance()

        
    def _rotateLeft(self, rotNode):
        """
        Descripción: Implementa la operación rotación a la izquierda 
        Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  izquierda
        Salida: retorna la nueva raíz


        EL hijo derecho (B) ahora es la raíz del árbol 
        la antigua raíz (A), es el hijo izquierdo de (B)
        Si (B) tenía un hijo izquierdo, pasa a ser el hijo derecho de (A)

        Ejemplo:

        Sentido de rotación <-

                A
        F               B
                    C       D
                              E

        Resultado:
                    B
            A               D
        F       C               E

        """

        newRoot = rotNode.rightnode

        rotNode.rightnode = newRoot.leftnode

        # Le copia el leftnode y actualiza su parent
        if newRoot.leftnode is not None:
            newRoot.leftnode.parent = rotNode

        newRoot.parent = rotNode.parent

        if rotNode.parent is None:
            # En este caso es la raíz del árbol
            self.root = newRoot
        else:
            # En este caso, rotNode puede ser el hijo derecho o izquierdo de su parent
            # en cualquier caso, actualizamos su referencia a newRoot
            if rotNode.parent.rightnode == rotNode:
                rotNode.parent.rightnode = newRoot
            else:
                rotNode.parent.leftnode = newRoot

        newRoot.leftnode = rotNode
        rotNode.parent = newRoot

        # El orden en que se actualizan los nodos importa, pues rotnNode es el hijo
        # de newRoot. Y para que newRoot tenga un bf correcto, la altura de rotNode
        # debe estar actualizada
        self._update_node(rotNode)
        self._update_node(newRoot)

    def _rotateRight(self, rotNode):
        """

        Descripción: Implementa la operación rotación a la derecha 
        Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  derecha
        Salida: retorna la nueva raíz

        El hijo izquierdo (B) ahora es la raíz del árbol
        La antigua raíz (A), es el hijo derecho de (B)
        Si (B) tenía un hijo derecho, pasa a ser el hijo izquierdo de (A)

        Ejemplo:
        Sentido de rotación ->
                        E
                C               F
            B       D
        A

        Resultado:
                        C
                B                E
            A                D        F


        """

        # 1) Nueva raíz
        newRoot = rotNode.leftnode

        # 2) Cambia a newRoot por su hijo derecho
        rotNode.leftnode = newRoot.rightnode

        # Y actualiza el parent del hijo copiado
        if newRoot.rightnode is not None:
            newRoot.rightnode.parent = rotNode

        # Le copia el parent
        newRoot.parent = rotNode.parent

        # Ahora hago checkeos sobre el parent
        # 1. Si rotNode es la raíz del árbol
        if rotNode.parent is None:
            self.root = newRoot

        # En este caso no es la raíz, por lo tanto hay que actualizar
        # la referencia del parent a newRoot
        else:
            if rotNode.parent.rightnode == rotNode:
                rotNode.parent.rightnode = newRoot
            else:
                rotNode.parent.leftnode = newRoot

        newRoot.rightnode = rotNode
        rotNode.parent = newRoot

        # El orden en que se actualizan los nodos importa, pues rotnNode es el hijo
        # de newRoot. Y para que newRoot tenga un bf correcto, la altura de rotNode
        # debe estar actualizada
        self._update_node(rotNode)
        self._update_node(newRoot)

    def _balance_node(self, node):
        
        """
        En caso de ser necesario aplica las rotaciones correspondientes para balancear 
        el nodo. 

        Nótese que el nodo solo va a poder ser balanceado en caso de que 
        el desbalance esa menor o igual a 2. Es por eso que el árbol se balancea 
        mediante una sucesión de balanceos de los nodos.

        Nótese que luego de realizar las rotaciones se deben calcular los bf
        """

        if node.bf < -1:
            
            # Double rotation requiered
            if node.rightnode is not None and node.rightnode.bf > 0:
                self._rotateRight(node.rightnode)
            
            self._rotateLeft(node)

        elif node.bf > 1:
            # Double rotation requiered
            if node.leftnode is not None and node.leftnode.bf < 0:
                self._rotateLeft(node.leftnode)
            
            self._rotateRight(node)
        else:
            raise Exception(f"Se está intentando balancear un nodo con un balance factor {node.bf}")

def traverse_breadth_first(tree) -> list:

    queue = [tree.root]

    nodes = []

    while len(queue):
        
        node = queue.pop(0)
        nodes.append(node)        
        
        if node.leftnode:
            queue.append(node.leftnode)
        if node.rightnode:
            queue.append(node.rightnode)

    return nodes