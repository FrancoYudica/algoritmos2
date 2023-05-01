import random


class DictUniversal:

    def __init__(self, m, p, max_hash_functions=None):

        self._used_coeffs = []
        self._max_hash_functions = max_hash_functions if max_hash_functions is not None else m
        self._p = p
        self._m = m

        self._table = [[] for _ in range(m)]

    def insert(self, key, value):

        if len(self._used_coeffs) < self._max_hash_functions:
            # Creates a new pair
            a = random.randrange(1, self._p)
            b = random.randrange(0, self._p)
            self._used_coeffs.append((a, b))

        else:
            a, b = self._used_coeffs[random.randrange(0, self._max_hash_functions)]

        hash_func = lambda k : ((a * k + b) % self._p) % self._m
        
        hash_value = hash_func(key)
        self._table[hash_value].append([key, value])

    def search(self, key):

        for a, b in self._used_coeffs:
            hash_func = lambda k : ((a * k + b) % self._p) % self._m
            hash_value = hash_func(key)

            for pair in self._table[hash_value]:
                if pair[0] == key:
                    return pair[1]

    def display(self):
        for i,l in enumerate(self._table):
            print(i, l)        


if __name__ == "__main__":
    d = DictUniversal(19, 21, 5)
    d.insert(4, "Franco")
    print(d.search(4))

    d.display()