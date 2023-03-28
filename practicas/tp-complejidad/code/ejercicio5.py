"""
Implementar un algoritmo Contiene-Suma(A,n) que recibe una
lista de enteros A y un entero n y devuelve True si existen en
A un par de elementos que sumados den n. Analice el costo computacional.
"""

def contains_add(numbers, n):

    """
    La idea del algoritmo se basa en complementos. 
    Por ejemplo:
        n = 21
        y tenemos la siguiente lista
            [6, 7, 2, 8, 9, 13, 1]
        se observa que 23 = 13 + 8. Por lo que el complemento con 13
        da 23 - 13 = 8. 
        Entonces, la idea es que para cada elemento de la lista vamos a 
        comprobar si su complemento se encuentra en la lista de complementos,
        en caso de que si, significa que si se encuentra la posible suma
    """

    complements = []

    for number in numbers:

        if number >= n:
            continue

        if number in complements:
            return True
        
        complements.append(n - number)

    return False

if __name__ == "__main__":
    l = [6, 7, 2, 8, 9, 13, 1]
    print(contains_add(l, 22))
