# crear lista con 10 números enteros
myList = [0,1,5,100,3,33,56,17,98,61]

# recorrer la lista con ciclo for e imprimir los resultados por consola
for i in myList:
    # con condicional if a su vez evaluar si el valor es par, impar o de valor "0"
    if i == 0:
        print("El numero es 0.")
    elif i % 2 == 0 :
        print(f"El numero {i} es par.")
    else:
        print(f"El numero {i} es impar.")