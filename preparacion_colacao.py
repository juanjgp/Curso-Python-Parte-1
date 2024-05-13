print("Proceso para preparar un colacao")

print("Paso 1: voy a la nevera y miro si hay leche")


leche = input("Paso 2: ¿Hay leche?: ")

if leche == "si":
    colacao = input("Paso 3: miro en el armario. ¿Hay colacao?: ")

    if colacao == "si":
        print("Paso 4: preparo el colacao")
        print("Paso 5: echo la leche")
        print("Paso 6: echo tres cucharadas de colacao")
        print("Paso 7: remuevo la mezcla")
        print("Paso 8: !para dentro¡")

    elif colacao == "no":
        print("Apunta colacao a la lista de la compra. Fin del programa.")

    else:
        print("Mal dicho. Fin del programa.")


elif leche == "no":
    print("Apunta leche a la lista de la compra. Fin del programa.")

else:
    print("Mal dicho. Fin del programa.")



