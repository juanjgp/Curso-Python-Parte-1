import random

numero=random.randint(1,10)

print("Adivina el número del 1 al 10")
numero_adivinado = int(input("Dime un número del 1 al 10: "))

if   1 <= numero_adivinado <=10:

    if numero_adivinado == numero:
        print("!Enhorabuena¡, has adivinado el número")

    else:
        print("Mala suerte, otra vez será, mi numero era el {}".format(numero))

else:
    print("Macho... Del 1 al 10 tronco")