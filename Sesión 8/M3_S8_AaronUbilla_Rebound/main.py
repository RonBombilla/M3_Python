my_list = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

# Crear una lista vacía para limpiar de duplicados
unify_list = []

# Función para ordenar y filtrar duplicados
def unify_elements():
    for i in my_list:
        if i not in unify_list:
            # Si "i" no existe en la lista, guarda el valor en "unify_list"
            unify_list.append(i)
    # Retornará la lista sin duplicados y ordenada de menor a mayor
    return sorted(unify_list)

# Imprimir resultados por consola
print(unify_elements())

