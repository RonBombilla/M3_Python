# Primero inicializo ambas variables a usar en la función
num1 = num2 = None

# Ahora creo la función que multiplicará ambas variables
def multi():
    # Le entrego los valores 20 y 30 a las variables respectivamente como lo pide el requerimiento
    num1, num2 = 20, 30
    # Inicializo la variable "res" que almacenará la multiplicación de ambos números
    res = num1 * num2
    # Luego retorno la variable "res" para poder imprimirla
    return res


# Finalmente imprimo con "print()" la función creada para mostrar el resultado en consola
print('El resultado de la multiplicación es: ', multi())
