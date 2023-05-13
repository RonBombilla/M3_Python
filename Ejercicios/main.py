passw = "123"

dato = input('Ingrese su contraseña: \n')

while dato != passw:
    print('Contraseña incorrecta! \n---------------------------------------')
    dato = input('Vuelva a ingresar su contraseña: \n')

print('Bienvenido')


numbers = [104, 4, 92, 1, 104, 64, 73, 99, 20]

mayor = numbers[0]

for i in numbers:
    if i > mayor:
        mayor = i
    #print(i)
    #print(mayor)

print('Maximum value:', mayor)


numLista = [25.50, 12.30, 36.40, 9.75, 15.20]
Sumatoria = sum(numLista)
total = (Sumatoria * 0.90)
print(f"La suma de la lista es: {total}")

