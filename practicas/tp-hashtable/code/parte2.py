from dictionary import Dictionary


def ejercicio3():
    """
    Considerar una tabla hash de tamaño m = 1000 y una función 
    de hash correspondiente al método de la multiplicación donde A = (sqrt(5)-1)/2).
    Calcular las ubicaciones para las claves 61,62,63,64 y 65.
    """
    m = 1000

    # Se utiliza el coeficiente recomendado por Donald Knuth
    a = (5**.5 - 1) * .5
    hash_func = lambda x: int(m * ((x * a) % 1))
    d = Dictionary(hash_func, m)
    keys = [61,62,63,64,65]
    for key in keys:
        d.insert(key, -1)

    d.display()


def ejercicio4_is_permutation(str1, str2):
    """
    Implemente un algoritmo lo más eficiente posible que devuelva True o False
    a la siguiente proposición: dado dos strings s1...sk  y p1...pk,
    se quiere encontrar si los caracteres de p1...pk corresponden a una permutación de
    s1...sk. Justificar el coste en tiempo de la solución propuesta.
    La complejidad de la implementación es de O(n) siendo n la cantidad de caracteres
    esto se debe a que iteramos 2 veces sobre todos los caracteres, realizando operaciones
    de insert, contains y delete, las cuales, gracias a trabajar con Dictionary son O(1),
    por lo tanto, la complejidad del algoritmo queda determinada por la complejidad de los bucles
    """
    # Con permutación se sabe que la cantidad de caracteres en el original y
    # el resutado debe ser la misma
    if len(str1) != len(str2):
        return False

    # Creo la función de hash de caracteres, utilizando el código ascii
    m = ord('z') - ord('a')
    hash_function = lambda char: ord(char) % m

    # Creo un diccionario que contiene todos los caracteres de str1
    d = Dictionary(hash_function, m)

    # Inserta todos los caracteres, sin importar las repeticiones, pues
    # la implementación de la tabla permite repeticiones
    for char in str1:
        d.insert(char, 1)

    is_permutation = True
    for char in str2:
        
        # Si se encuentra el caracter
        if char in d:
            # Lo borro, por las repeticiones
            d.delete(char)
        else:
            is_permutation = False
            break

    return is_permutation

def ejercicio5_unique_elements(linked_list: list):

    """
    Implemente un algoritmo que devuelva True si la lista que recibe de 
    entrada tiene todos sus elementos únicos, y Falso en caso contrario.
    Justificar el coste en tiempo de la solución propuesta.
    La complejidad del algoritmo es O(n). 
    Primero cargo la lista en Dictiorary, operación O(n)
    Luego itero por cada uno de los elementos de la lista O(n),
    pero por cada key, itero por la estructura de datos del Diccionario O(c),
    donde c es el factor de carga, el factor de carga es menor que n, luego
    la complejidad resulta O(n)
    """

    # La idea es cargar la HashTable con todos los elementos de la lista,
    # luego, acceder a cada uno de los elementos de la lista y verificar
    # si la key es unica en cada una de las sub-listas

    m = len(linked_list)
    a = (5**.5 - 1) * 0.5 
    hash_func = lambda x: int(m * ((x * a) % 1))
    hash_table = Dictionary(hash_func, m)

    for key in linked_list:
        hash_table.insert(key, None)

    for key in linked_list:
        sub_list = hash_table.table[key]
        found = False
        # Cuenta la cantidad de repeticiones de la key
        for node in sub_list:
            if node[0] == key:
                # Si ya se encontraba en la lista entonces estaba repetida
                if found > 1:
                    return False
                found = True

    return True

if __name__ == "__main__":
    print(ejercicio5_unique_elements([1, 2, 3, 3]))