# Calcular el factorial de un número con ciclo while
from math import gamma
number = float(input('Ingrese un número entero para calcular su factorial: '))
while number <= 0:
    number = float(
        input('Ingrese un número entero para calcular su factorial: '))

# Crear variable que almacenará el resultado
fact = 1
i = 1

while i <= number:
    fact = fact * i
    i = i + 1

# Imprimir por consola la variable con el resultado
print(f'El factorial del número {number} es {fact}')


# --------------------------------------------------------------------------------------------------------

# Calcular factorial con el módulo "math.gamma" que a diferencia de "gamma.factorial" si permite números decimales

result = float(gamma(number + 1))

# Imprimir por consola el resultado
print(f'El factorial del número {number} es {result}')

# ---------------------------------------------------------------------------------------------------------


# Calcular factorial con ciclo for
def calcularfactorial():
    fact = 1
    # Redondear o transformar a entero "number" por que en rango no permite decimal
    for i in range(1, round(number) + 1):
        fact *= i
    return fact


# Imprimir por consola el resultado
print(f'El factorial del número {number} es {calcularfactorial()}')
