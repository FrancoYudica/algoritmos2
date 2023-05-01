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
        print(f"Key={key} hash: {hash_func(key)}")

    d.display()



"""
Implemente un algoritmo lo más eficiente posible que devuelva True o False
a la siguiente proposición: dado dos strings s1...sk  y p1...pk,
se quiere encontrar si los caracteres de p1...pk corresponden a una permutación de
s1...sk. Justificar el coste en tiempo de la solución propuesta.
"""

def ejercicio4_is_permutation(str1, str2):

    """
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

    # Inserta todos los caracteres, y como valor le pongo la cantidad de repeticiones
    for char in str1:

        if char in d:
            d[char] += 1
        else:
            d.insert(char, 1)

    for char in str2:
        
        # Si se encuentra el caracter
        if char in d:
            
            # Disminuyo la cantidad de repeticiones
            d[char] -= 1
            if d[char] == -1:
                return False
        else:
            return False
        
    return True


"""
Ejercicio 5
Implemente un algoritmo que devuelva True si la lista que recibe de 
entrada tiene todos sus elementos únicos, y Falso en caso contrario.
Justificar el coste en tiempo de la solución propuesta.
"""
def unique_elements(linked_list : list):

    """
    La complejidad resulta O(n):
        - Itero por todos los elementos O(n)
        - Uso la función search O(c)
        - Inserto O(1)
    """
    # Defino la función de hash
    m = len(linked_list)
    a = (5**(0.5)-1.0) * 0.5
    hash_func = lambda x: int(((a * x) % 1) * m)
    hash_table = Dictionary(hash_func, m)

    # Itero por los elementos de la lista
    for element in linked_list:

        # Si el elemento ya ha sido insertado
        if element in hash_table:
            return False
        
        # Agrego el elemento por primera vez
        hash_table.insert(element, 1)

    return True


"""
Los nuevos códigos postales argentinos tienen la forma cddddccc,
donde c indica un carácter (A - Z) y d indica un dígito 0, . . . , 9.
Por ejemplo, C1024CWN es el código postal que representa a la calle XXXX
  a la altura 1024 en la Ciudad de Mendoza. 
Encontrar e implementar una función de hash apropiada para
los códigos postales argentinos
"""
def ejercicio6():
    m = 1009    
    code = "a1016idb"
    
    def hash_postal(code):
        # Trato de que el código hash de lugares cercanos sea similar, es por 
        # eso que considero:
        # - El primer caracter como la ciudad
        # - Los dddd como la altura
        # - Los ccc como la calle
        # Entonces debo evaluar primero los c y luego los d, de esta manera 
        # garantizo que los códigos postales de lugares cercanos sean cercanos
        # Entonces la cuidad y la calle deben tener mas peso que la altura

        val = ord(code[0]) * 10_000     # Ciudad
        val += ord(code[5]) * 1_000     # Calle
        val += ord(code[6]) * 100       # Calle
        val += ord(code[7]) * 10        # Calle
        val += int(code[1:5])           # Altura

        return val % m

    print(hash_postal(code))


"""
Implemente un algoritmo para realizar la compresión básica de
cadenas utilizando el recuento de caracteres repetidos.
La complejidad del algoritmo es O(n), pues se itera una sola
vez por la lista de n elementos
"""
def ejercicio7_compresion(patron):

    compressed = ""

    char = patron[0]
    count = 0

    for i in range(len(patron)):

        # Si nos encontramos con el mismo char
        if char == patron[i]:
            # Se incrementa su contador
            count += 1
        
        # Cuando nos encontramos con otro
        else:
            # Agregamos los resultados comprimidos
            compressed += char + str(count)

            # Iniciamos el contador con el otro char
            char = patron[i]
            count = 1

    # Agregamos el final
    compressed += char + str(count)

    # Retorno el patron o el comprimido, selecciono el mas corto
    return patron if len(compressed) >= len(patron) else compressed


"""
Se requiere encontrar la primera ocurrencia de un string p1...pk
en uno más largo a1...aL. Implementar esta estrategia de la forma
más eficiente posible con un costo computacional menor a O(K*L)
(solución por fuerza bruta).  Justificar el coste en tiempo de la
solución propuesta.
"""
def ejercicio8_optimized(text, pattern):

    # La complejidad de este algoritmo es de O(n), siendo
    # n la cantidad de caracteres de 'text', pues solo itero
    # una vez por la cadena 'text'
    
    matches = 0
    start_index = -1
    i = 0

    while i < len(text):

        # Cuando se obtiene una coincidencia 
        if text[i] == pattern[matches]:

            # Almacena el primer índice                
            if matches == 0:
                start_index = i

            matches += 1
            # Esto significa que el patron fue encontrado
            if matches == len(pattern):
                return start_index
            
            # Todavia no termina, siguie evaluando
            i += 1
        else:
            
            # Cuando el anterior caracter coincide, pero este no
            if matches > 0:
                matches = 0
                start_index = -1
                # No se incrementa el contador, para que el caracter
                # actual entre en el bucle de comparación y no se saltee
            
            # Caso contrario, se incrementa normalmemte
            else:
                i += 1


def ejercicio8_hashtable(text, pattern):
    # Complejidad O()
    # La idea de este método, es ir agregando
    # las sub-cadenas del texto de la misma longitud
    # que las de pattern, de manera secuencial.

    # Hash function toma los primeros tres caracteres del patron p
    # (en caso de que tenga esa cantidad de caracteres, por eso uso min)
    # nótese que también se multiplican por potencias de 10
    m = 17
    hash_function = lambda p: sum([ord(p[i]) * 10 ** i for i in range(min(3, len(p)))]) % m

    dictionary = Dictionary(hash_function, m)
    pattern_length = len(pattern)    

    for i in range(0, len(text) - pattern_length + 1):

        # Creo el patron de la misma longitud que pattern
        sub_pattern = text[i : i + pattern_length]

        # Lo inserto en el diccionario con su respectivo índice
        dictionary.insert(sub_pattern, i)
        
    # Se se encuentra, retorno el índice, de otra manera None
    return dictionary[pattern] if pattern in dictionary else None

"""
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}.
Implemente un algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T).
¿Cuál es la complejidad temporal del caso promedio del algoritmo propuesto?
"""
def ejercicio9(subset_list, set_list):


    # En la implementación asumo que no hay repetición de elementos, es una de las propiedades
    # de los conjuntos. La complejidad del algoritmo que propongo es de O(n), siendo n la
    # cantidad de elementos del conjunto
    
    # El 'subconjunto' no puede tener mas elementos
    if len(subset_item) > len(set_list):
        return False

    # Creo la función de hash con el módulo
    m = 109
    hash_func = lambda x: x % m
    set_dictionary = Dictionary(hash_func, m)

    # Cargo el conjunto en el diccionario
    for item in set_list:
        set_dictionary.insert(item, -1)

    # Itero por los elementos del 'subconjunto'
    for subset_item in subset_list:
        
        # Si lo contiene
        if set_dictionary.contains(subset_item):
            # Lo elimino
            set_dictionary.delete(subset_item)

        # Si no lo contiene, entonces no es subconjunto
        else:
            return False
        
    return True



if __name__ == "__main__":  
    print(ejercicio4_is_permutation("abcdef", "badcef"))
    #print(ejercicio8_hashtable("abracadabra", "dabra"))
    #ejercicio4_is_permutation()
    #print(ejercicio9([1, 2, 3], [1, 6, 3, 4]))