texto = "Test sobre el champi"
print(texto)
print("-" * len(texto))
print(" ")
puntuacion = 0

print("Pregunta 1: ¿Que haces cuando ves un champi?:\n"
      
      "\nOpcion A: lo miro con recelo y algo de inquina si está crudo.\n"
      "Opcion B: lo miro con lujuria y pasión y me dan ganas de comermelo hasta crudo.\n"
      "Opcion C: salgo corriendo todo lo que puedo y si tuviera una nave espacial acababa en la luna.\n")

respuesta_1 = (input("Elige una opción: "))
respuesta_1 = respuesta_1.upper()

if respuesta_1 == "A":
    puntuacion += 5

elif respuesta_1 == "B":
    puntuacion += 10

elif respuesta_1 == "C":
    puntuacion += 0

else:
    print("Tu eres tonto, responde bien anda.")
    exit()


print("Pregunta 2: ¿Cómo te gusta la pizza?:\n"

      "\nOpcion A: con todo y más, y si lleva champis canto una saeta de celebración.\n"
      "Opcion B: como le pongan champis la esclafo contra la pared, pero si tiene piña no.\n"
      "Opcion C: pocos ingredientes pero valientes. Si le añaden champi, no me quejo del todo, echo una lagrimilla.\n")

respuesta_2 = (input("Elige una opción: \n"))
respuesta_2 = respuesta_2.upper()

if respuesta_2 == "A":
    puntuacion += 10

elif respuesta_2 == "B":
    puntuacion += 0

elif respuesta_2 == "C":
    puntuacion += 5

else:
    print("Tu eres tonto, responde bien anda.")
    exit()

print("Pregunta 3: ¿Te gustaría trabajar en una empresa de champi?:\n"

      "\nOpcion A: fua flipante lo de allí, máquinas, instalación y sobre todo la gente.\n"
      "Opcion B: buenoooo... habrá que pagar la hipoteca ¿no?.\n"
      "Opcion C: es ver una empresa de champi en el horizonte y se comen los demonios.\n")

respuesta_3 = (input("Elige una opción: \n"))
respuesta_3 = respuesta_3.upper()

if respuesta_3 == "A":
    puntuacion += 10

elif respuesta_3 == "B":
    puntuacion += 5

elif respuesta_3 == "C":
    puntuacion += 0

else:
    print("Tu eres tonto, responde bien anda")
    exit()


print("La puntuación final es de: {}\n".format(puntuacion))

if puntuacion >= 25:
    print("Eres un fanático del champi. Con él alucinas pepinillos.")

elif 10 <= puntuacion < 25:
    print("El champi te gusta pero si desaparece de tu vida tu sigues igual de reluciente.")

elif puntuacion < 10:
    print("Eres alérgico al champi. Mejor ni lo huelas.")