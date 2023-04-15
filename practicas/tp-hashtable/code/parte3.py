

empty_value = 'deleted-none'


def insert(table, hash_func, key, value):
    m = len(table)

    for i in range(len(table)):
        index = hash_func(key, i)
        if table[index] == empty_value:
            table[index] = value
            return


def ejercicio10():
    m = 11
    table = [empty_value for _ in range(m)]
    keys = [10, 22, 31, 4, 15, 28, 17, 88, 59]
    h = lambda k: k

    # Linear probing hash function
    linear_probing = lambda k, i: (h(k) + i) % m

    c1 = 1
    c2 = 3

    # Quadratic probing hash function
    quadratic_probing = lambda k, i: (h(k) + c1 * i + c2 * i * i) % m

    # Double hasing 
    h2 = lambda k: 1 + (k % (m - 1))
    double_hashing = lambda k, i: (h(k) + i * h2(k)) % m

    for key in keys:
        insert(table, linear_probing, key, key)

    print(table)


def ejercicio11():
    m = 10
    table = [empty_value for _ in range(m)]
    keys = [12, 18, 13, 2, 3, 23, 5, 15]
    h = lambda k: k

    # Linear probing hash function
    linear_probing = lambda k, i: (h(k) + i) % m
    for key in keys:
        insert(table, linear_probing, key, key)

    print(table)


if __name__ == "__main__":  
    ejercicio11()
