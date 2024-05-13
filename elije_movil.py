print("Elije tu teléfono móvil\n")

operativo = input("¿Qué sistema operativo quieres?: iOS o android ")

operativo = operativo.lower()

if operativo == "android":

    dinero = input("¿Tienes dinero?: S/N ")
    dinero = dinero.lower()
    if dinero == "s" or dinero == "si":
        camara = input("¿Te importa la cámara del móvil?: S/N ")
        camara = camara.lower()
        if camara == "s" or camara == "si":
            print("Elige el Google Pixel Supercamara")
        elif camara == "n" or camara == "no":
            print("Píllate un Android calidad-precio")
        else:
            print("!Te dije que respondieras si o no¡ perdona... ¿es usted tonto? eeeeh ")
    elif dinero == "n" or dinero == "no":
        print("El android chino de 100 € es la polla para tí")
    else:
        print("!Te dije que respondieras si o no¡ perdona... ¿es usted tonto? eeeeh ")

elif operativo == "ios":

    dinero = input("¿Tienes dinero?: S/N ")
    dinero = dinero.lower()
    if dinero == "s" or dinero == "si":
        print("Pillate el iPhone Ultra Pro Max")
    elif dinero == "n" or dinero == "no":
        print("Pillate el iPhone cutre de segunda mano")
    else:
        print("!Te dije que respondieras si o no¡ perdona... ¿es usted tonto? eeeeh ")

else:
    print("\n¿Qué sistema operativo es ese?. !Te vas a reir de tu puta madre¡")