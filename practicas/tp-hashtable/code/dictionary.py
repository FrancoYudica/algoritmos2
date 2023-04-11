

class Dictionary:
    def __init__(self, hash_function=None, slots=None):

        # Defines the hash function, if not provided
        # In this implementation, the default is the module fuction
        # The table contians n slots

        if slots is None:
            slots = 9

        if hash_function is None:
            self.hash_function = lambda x : x % slots
        
        else:
            self.hash_function = hash_function


        # Initializes the table, in each slot an empty linked list is initialized
        self.table = [[] for _ in range(slots)]

    def insert(self, key, value):
        """Insertion. Appends the tuple (key, value) to the corresponding list"""
        hash_value = self.hash_function(key)
        self.table[hash_value].append((key, value))


    def search(self, key):
        """Given the key of the element, tries to find it's
        value inside the corresponding list"""
        hash_value = self.hash_function(key)

        linked_list = self.table[hash_value]

        for node in linked_list:
            node_key = node[0]
            if node_key == key:
                return node[1]
            

    def delete(self, key):
        """Removes the element from the list"""
        hash_value = self.hash_function(key)
        linked_list = self.table[hash_value]

        # Tries to find the key inside the 
        node_index = -1

        for i, node in enumerate(linked_list):
            node_key = node[0]
            if node_key == key:
                node_index = i
                break
            
        if node_index == -1:
            return 
        
        del linked_list[node_index]

    def display(self):
        for i, l in enumerate(self.table):
            message = f"[{i}]" + repr(l)
            print(message)
