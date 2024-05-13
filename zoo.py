print("Tarifas del 25% de descuento para entrar al zoo")

edad = int(input("Dime cuántos años tienes: "))

estudiante = input("¿Tienes carnet de estudiante?: ")

familia = input("¿Tienes carnet de familia numerosa?: ")

pensionista = input("¿Tienes carnet de pensionista?: ")

if edad <= 10 or edad >= 65 or estudiante == "si" or familia == "si" or pensionista == "si":
    print("Tienes un descuento del 25% en la entrada del zoo")

else:
    print("Nada macho a apoquinar el importe íntegro")