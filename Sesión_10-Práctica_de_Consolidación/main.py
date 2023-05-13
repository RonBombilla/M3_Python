magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = ["Messi", "Pele", "Juanes"]

#magos_grandiosos = []


def hacer_grandioso():
    for i in range(len(magos)):
        magos[i] = 'El gran ' + magos[i]
    # for i in magos:
    #     magos_grandiosos.append("El gran " + i)


def imprimir_nombres(lista):
    for i in lista:
        print(i)


print("---------------")
imprimir_nombres(magos)
print("---------------")
hacer_grandioso()
imprimir_nombres(magos)
#imprimir_nombres(magos_grandiosos)
print("---------------")
imprimir_nombres(cientificos)
print("---------------")
imprimir_nombres(otros)
print("---------------")
