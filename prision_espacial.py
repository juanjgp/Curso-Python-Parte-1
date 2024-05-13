import random
titulo = "escapada de la prisión espacial"
print("Escapada de la prisión espacial")
print("-" * len(titulo))
print("")

print("Sinopsis: Tu y tu compañero de celda os acabais de escapar de la prisión espacial.\n"
      "Habéis burlado a los guardias y os dirijís hacia el exterior y entrais en una mazmorra.\n"
      "Un guardia os pilla y ataca a tu compañero, pero tu te escondes, tu compañero ha caido.\n"
      "!Tienes que escapar¡.\n")

print("Al salir del escondite te encuentras una puerta semiabierta y una escotilla, debes tomar una de ellas.\n"
      "¿Que opción eliges?: \n"
      "Opción A-Puerta semiabierta.\n"
      "Opción B-Escotilla.\n")

salida = input("Opción: ")
salida = salida.upper()

if salida == "A":
      print("Tomas la puerta semiabierta y más adelante te encuentras un guardia alienígena con un sombrero vikingo.\n"
            "Tienes dos opciones: \n"
            "Opcion A-Te haces el dormido.\n"
            "Opción B-Huyes despavoridamente sin mirar atrás.\n")

      guardia = input("Opción: ")
      guardia = guardia.upper()

      if guardia == "A":
            print("Te haces el dormido pero el guardia que es alienígena tiene un poder maravilloso para detectar mentirosos\n"
                  "inútiles como tú. !TU JUEGO SE HA ACABADO¡.")

      elif guardia == "B":
            print("Huyes despavoridamente hasta encontrar la salida y te esperan en la puerta 7 alienígenas hembra vírgenes. !TU JUEGO SE HA ACABADO¡ a lo grande.")

      else:
            print("Te pones a hacer el payaso y al guardia le gusta. Pero era una trampa. !HAS MUERTO¡.")




elif salida == "B":
      print("Tomas la escotilla, caes a una zona inundada. El agua te llega hasta las rodillas, avanzas una media hora hasta llegar a una zona abierta, seca y con luz.\n"
            "Típico claro de las alcantarillas, que tiene varios caminos. Hay un palo tirado en ese sitio.\n")
      coger_palo = input("¿Lo coges?: si/no ")

      if coger_palo == "si":
            print("Has cogido el palo.\n")
            palo = True

      elif coger_palo == "no":
            print("No has cogido el palo.\n")
            palo = False
      else:
            print("Lo tomas o lo dejas Carl. Mientras te decides. Un monstruo de las alcantarillas, llamemoslo el chupachota, te come y todo se acaba.")
            exit()

      print("Sigues adelante y te encuentras una rata de dos metros, tiene un kimono la jodia rata, no me preguntes porqué.\n"
            "La rata que acababa de sacarse el título de matemáticas te pide que respondas bien a la siguiente operación aritmética:\n")

      print("Cuanto es:\n")
      aleatorio = int(random.randint(1,100))
      valor = 13 * aleatorio
      resultado = float(input("13 por {} ".format(aleatorio)))

      if resultado == valor:
            print("Continúa tu andadura...")

      else:
            print("Continuas por aquí...")

 



else:
      print("!Tienes que elegir escotilla o puerta¡. Tu que vas de guay por la vida. Ala te pilla un guardia y !!!MUERTO¡¡¡.")