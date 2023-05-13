num = int(input("Introduce un número: "))

if num == 0:
    print("El número es cero")
elif num > 0:
    if num % 2 == 0:
        print("El número es positivo y par")
    else:
        print("El número es positivo e impar")
else:
    if num % 2 == 0:
        print("El número es negativo y par")
    else:
        print("El número es negativo e impar")
