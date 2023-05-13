option = None

while option != 0:

    option = int(input("Ingresa un número del 1 al 5\n"))

    match option:

        case 1:
            print("Morirás")
        case 2:
            print("Comida de regalo")
        case 3:
            print("$1000 de regalo")
        case 4:
            print("Te caiste wey")
        case 5:
            print("Celu al agua")
        case 0:
            print("Adios")
            break
