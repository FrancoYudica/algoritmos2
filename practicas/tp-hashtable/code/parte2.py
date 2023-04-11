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
    """

    if len(str1) != len(str2):
        return False
    
    # Una manera seria insertar todas las permutaciones posibles de 


def ejercicio5_unique_elements(linked_list: list):

    """
    Implemente un algoritmo que devuelva True si la lista que recibe de 
    entrada tiene todos sus elementos únicos, y Falso en caso contrario.
    Justificar el coste en tiempo de la solución propuesta.
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
        sub_list = hash_table.table[hash_func(key)]
        
        for sub_key in sub_list:
            if sub_key == key:
                return False


if __name__ == "__main__":
    ejercicio3()