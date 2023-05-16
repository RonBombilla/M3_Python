
# Crear una función que acepte 3 números como parámetros
def three_numbers(a, b, c):
    # sumar todos los valores 
    total_sum = a + b + c
    # y adicionalmente reste el segundo y tercer parámetro al primero.
    total_res = a - (b + c)
    # El resultado debe ser almacenado en una tupla
    result_tupla = (f'La suma total es: {total_sum} \nLa resta del 1°, menos el 2° y 3° número es: { total_res}')
    return result_tupla

# Solicitar datos y guardarlos en una lista
num1 = float(input('ingresa un número: '))
num2 = float(input('ingresa otro número: '))
num3 = float(input('ingresa el último número: '))

lista = [num1, num2, num3]

#Pasar como parametros los números almacenados en la lista
print(three_numbers(lista[0], lista[1], lista[2]))
