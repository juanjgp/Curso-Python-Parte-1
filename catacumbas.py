import random

titulo = "las catacumbas olvidadas"
print("Las catacumbas olvidadas")
print("-" * len(titulo))
print("")

print("Introducción:\n"
      "Te encuentras dando un paseo por tu pueblo o ciudad, vas a las afueras y ves que\n"
      "una casa abandonada a las afueras tiene una puerta abierta que antes no estaba.\n"
      "\n¿Qué haces?:\n"
      "\nA-Decides echarle todo el valor del mundo porque te mola la aventura y pasas.\n"
      "B-Te largas y sigues tu camino porque te ha dado una pizca de miedito.\n")

entrada = input("Decide: ")
entrada = entrada.upper() #Esto es por si se escribe la opción en minúscula

if entrada == "A":
    print("\nDecides entrar y ves todo muy decadente y algo oscuro.\n"
          "De repente, notas que has pisado algo parecido a un trozo de cristal bien afilado.\n"
          "\n¿lo coges?:\n"
          
          "\nA-Si, por si las moscas.\n"
          "B-No, no vaya ser que me haga un cortecillo y tengamos un disgusto.\n")

    coger_cristal = input("Tu dirás: ")
    coger_cristal = coger_cristal.upper()

    if coger_cristal == "A":
        print("Coges el cristal\n")
        cristal = True

    elif coger_cristal == "B":
        print("No coges el cristal\n")
        cristal = False
    else:
        print("Te pasas tanto tiempo pensando si cogerlo o no que la casa colapsa y ahí te quedas.\n"
              "\nFIN")
        exit()

    print("Más adelante bajas unas escaleras, todo se derrumba detrás de ti y no encuentras salida.\n"
          "Descubres como una especie de catacumbas donde hay huesos de antiguos arbitros \n"
          "que pitaban mal en los partidos de fútbol del equipo local.\n"
          "\nUno de esos arbitros toma vida en forma de esqueleto y se ve que no tiene otra cosa mejor que hacer\n"
          "que pedirte que le resuelvas la siguiente duda:\n")

    print("Necesito recordar en que año pité el partido fatal y me llevó a la tumba tirandome los habitantes por un barranco.\n"
          "Para ello resuelve la siguiente operación:\n")

    aleatorio = random.randint(1,10)
    valor = 200 * aleatorio
    respuesta = int(input("200 multiplicado por {}: ".format(aleatorio)))

    if respuesta == valor:
        print("Has acertado. El esqueleto te permite pasar a la siguiente sala donde encuentras un silbato de arbitro tirado en el suelo.\n"
              "\n¿Lo coges?:\n"
              "\nA-No, podría ser útil después, pero me da mala espina.\n"
              "B-Si, podría hacerlo sonar para abrir un pasadizo o algo que me permita salir de aquí.\n")
        silbato = input("¿Que haces?: ")
        silbato = silbato.upper()

        if silbato == "B":
            print("Haces sonar el silbato, pero resulta que estaba maldito y te acabas convirtiendo en un arbitro esquelético más.\n"
                  "\nFIN")

        elif silbato == "A":
            print("Ahí se queda el silbato y puedes continuar hasta una puerta con una extraña hendidura.\n"
                  "Ahí descubres que:\n"
                  "El cristal encaja ahí\n")

            if cristal == True:
                print("TIENES EL CRISTAL\n")
                print("Perfecto, el cristal encaja, escapas de las catacumbas y de paso vuelves a tu casa a lomos de un centauro\n"
                      "que se convierte en tu animal de compañía Y VIVES FELIZ Y CON ENTUSIASMO.\n"
                      "\nFIN A TOPE")

            if cristal == False:
                print("NO TIENES EL CRISTAL\n")
                print("\nVuelves a por el cristal pero los esqueletos de los arbitros resucitan y te invitan a una copa de coñac.\n"
                      "Te lo tomas pensando que son tus colegas pero estaba envenenado y te acabas convirtiendo en uno de ellos. "
                      "Con silbato incorporado.\n"
                      "\nFIN")

        else:
            print("En este juego hay que responder claramente, si no el resto son palabras mágicas que reviven a todos los arbitros\n"
                  "y se montan una buena juega contigo. Vamos que te han aniquilao. FIN")


    elif respuesta != valor:
        print("Has fallado hasta teniendo la calculadora en el móvil eres tan inútil que el esqueleto sufre vergüenza ajena y te manda al \n"
              "infierno de cabeza y a pasar la vida al calorcito. No es un mal final porque no pasas frío pero no es lo que quieres.\n"
              "\nFIN")

elif entrada == "B":
    print("\nPasas del tema y vas caminando hasta llegar a una carretera.\n"
          "Ves que pasa un coche con una gente que viene de darlo todo de fiesta, y descubres que\n"
          "son tus colegas que vienen de una rave. Les pides que te acerquen al pueblo.\n"
          "Llegas a tu casa otro día aburrido más.\n"
          "\nFIN")
else:
    print("Tronco te pedido opción A o B, ahora por listo aparece un ninja salvaje y acaba contigo.\n"
          "\nFIN")
