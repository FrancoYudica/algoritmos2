"""
Implementar un algoritmo que ordene una lista de elementos 
donde siempre el elemento del medio de la lista contiene 
antes que él en la lista la mitad de los elementos menores que él.
Explique la estrategia de ordenación utilizada.
"""

# Lo primero que voy a hacer es encontrar el valor medio de la lista de entrada,
# de esta manera me aseguro que van a existir elementos mas grandes y mas chicos
# para llevar a cabo tal tarea, voy a utilizar un algoritmo de ordenamiento y luego
# retirar el emenento del medio de la lista
a = [4, 5, 7, 1, 2, 6, 10, 8, 9, 3]

sorted_list = sorted(a)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
middle_index = len(sorted_list) // 2 - 1  # 10 // 2 - 1 = 4
middle_value = sorted_list[middle_index]

greater = sorted_list[middle_index+1:]
smaller = sorted_list[:middle_index]
smaller_count = len(smaller)
greater_count = len(greater)

# El índice del valor medio en la nueva lista debe ser el mismo
half_smaller = smaller_count // 2
half_greater = greater_count // 2

result = smaller[:half_smaller] + greater[:half_greater] + [middle_value] + smaller[half_smaller:] + greater[half_greater:]
print(result)

