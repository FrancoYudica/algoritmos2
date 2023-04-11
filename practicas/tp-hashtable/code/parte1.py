"""
Ejemplificar que pasa cuando insertamos las llaves 5, 28, 19, 15, 20,  33, 12, 17, 10 
en un HashTable con la colisión resulta por el método de chaining.
Permita que la tabla tenga 9 slots y la función de hash:
    h(x) = x % 9

"""
import dictionary

if __name__ == "__main__":

    d = dictionary.Dictionary(
        hash_function=lambda x: x % 9,
        slots=9
        )
    keys = [5, 28, 19, 15, 20, 33, 12, 17, 10]
    shared_value = -1
    for key in keys:
        d.insert(key, shared_value)

    d.display()