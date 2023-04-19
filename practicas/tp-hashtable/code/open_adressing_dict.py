

class OpenAdressingDict:


    # Initialization functions for all the probing methods
    def initialize_linear_probing(self, aux_hash, m):
        self.m = m
        self.hash_function = lambda k, i : (aux_hash(k) + i) % self.m
        self._initialize_table()

    def initialize_quadratic_probing(self, aux_hash, c1, c2, m):
        self.m = m
        self.hash_function = lambda k, i : (aux_hash(k) + c1 * i + c2 * i * i) % self.m
        self._initialize_table()

    def initialize_double_hashing(self, aux_hash1, aux_hash2, m):
        self.m = m
        self.hash_function = lambda k, i : (aux_hash1(k) + aux_hash2(k) * i) % self.m
        self._initialize_table()

    def _initialize_table(self):
        # Creates the empty table of length self.m, so self.m should be initialized
        self.table = [(None, None) for _ in range(self.m)]

    def insert(self, key, value):

        for i in range(self.m):
            hash_value = self.hash_function(key, i)

            table_tuple = self.table[hash_value]
            tuple_key = table_tuple[0]

            if tuple_key is None or tuple_key == "deleted_element":
                self.table[hash_value] = (key, value)
                return
        
        # No slot available
        raise Exception("Hash overflow")

    def search(self, key):

        for i in range(self.m):
            hash_value = self.hash_function(key, i)
            table_tuple = self.table[hash_value]
            tuple_key = table_tuple[0]

            if tuple_key == key:
                return table_tuple[1]
            
            if tuple_key is None:
                return None
    
    def delete(self, key):

        for i in range(self.m):
            hash_value = self.hash_function(key, i)

            if self.table[hash_value][0] == key:
                self.table[hash_value] = ("deleted_element", None)
                return True
            
        return False
    
    def contains(self, key):
        for i in range(self.m):
            hash_value = self.hash_function(key, i)

            if self.table[hash_value][0] == key:
                return True
        return False

    def display(self):
        for i in range(self.m):
            print(f"[{i}]: {self.table[i]}")

    # Operator overloading
    def __getitem__(self, key):
        sucess = self.search(key)
        if sucess is None:
            raise Exception(f"Key: ({key} not found)")
        return sucess
    
    def __setitem__(self, key, value):

        # If already stored, modifies the value
        if self.contains(key):
            # Finds the key and modifies the value
            for i in range(self.m):
                hash_value = self.hash_function(key, i)

                if self.table[hash_value][0] == key:
                    self.table[hash_value] = (key, value)
                    return

            # Shouldnt get here
            assert False       

        # Otherwise inserts
        self.insert(key, value)

    def __contains__(self, key):
        return self.contains(key)

if __name__ == "__main__":
    hash_function = lambda pattern : sum([ord(pattern[i]) * 10 ** i for i in range(min(3, len(pattern)))])
    dictionary = OpenAdressingDict()
    dictionary.initialize_linear_probing(hash_function, 21)

    dictionary["Hello"] = 11
    dictionary["Babe"] = 13
    dictionary["Babs"] = 13
    dictionary["Babd"] = 15
    dictionary.display()

    print(f"Does dict contain('Babs')? : {'Babs' in dictionary}")
    print(f"Delete sucess: {dictionary.delete('Babs')}")
    print(f"Does dict contain('Babs')? : {'Babs' in dictionary}")

    dictionary.display()
    print(f"Search value of key 'Babd': {dictionary['Babd']}")
