# ingresar números a evaluar
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# introducir los números en una lista
myList = [num1,num2,num3]

# ordenar los números de la lista con el metodo "sort()"
myList.sort(reverse=True)
# imprimir por consola los datos ordenados
print(myList)