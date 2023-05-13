# Adivina el número antes que acaben los intentos
import random

intentos = 0
numero = random.randint(1, 10)
print('Adivina el número entre 1 y 10 que nuestra IA de última generación está pensando!')

while intentos < 5:

    respuesta = int(input('Que número crees que puede ser? : \n '))
    print('--------------------- \n')
    intentos = intentos + 1

    if intentos == 5:
        break

    elif respuesta > numero:
        print(f'Te pasaste güerito, intentos restantes: {5 - intentos}...')
        print('Intenta con otro número! \n ------------------------')

    elif respuesta < numero:
        print(f'Te quedaste corto güerito, intentos restantes {5 - intentos}...')
        print('Intenta con otro número! \n ------------------------')

    elif respuesta == numero:
        break

if respuesta == numero:
    print('Le atinaste a la marrana! Bien hecho!\n ------------------------')
    print('Gracias por participar!')
    print('Besito *3*')

elif respuesta != numero or intentos == 5:
    print('Fallaste, no te quedan intentos perdedor!')
    print('Deshonrrar a tu Vaca ' + '\U0001F432')