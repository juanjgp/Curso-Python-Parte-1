titulo = "Conversor de divisas"

print("Conversor de divisas")
print("-" * len(titulo))
print(" ")

euro_dolar = 1.1
dolar_euro = 0.91
euro_libra = 0.85
libra_euro = 1.17

print("¿Qué cambio de divisa deseas hacer?\n"
               "A. De euro a dolar.\n"
               "B. De dolar a euro.\n"
               "C. De euro a libra.\n"
               "D. De libra a euro.\n")

divisa = input("Elige una opción: ")

divisa = divisa.upper()

if divisa == "A":
    conversor = euro_dolar
    euros = float(input("Dime el valor en euros € a convertir en dolares $: "))
    dolares = conversor * euros
    print("El valor en dolares de {} euros es de : {} $".format(euros, dolares))

elif divisa == "B":
    conversor = dolar_euro
    dolares = float(input("Dime el valor en dolares $ a convertir en euros €: "))
    euros = conversor * dolares
    print("El valor en euros de {} dolares es de : {} €".format(dolares, euros))

elif divisa == "C":
    conversor = euro_libra
    euros = float(input("Dime el valor en euros € a convertir en libras: "))
    libras = conversor * euros
    print("El valor en libras de {} euros es de : {} libras".format(euros, libras))

elif divisa == "D":
    conversor = libra_euro
    libras = float(input("Dime el valor en libras a convertir en euros €: "))
    euros = conversor * libras
    print("El valor en euros de {} libras es de : {} €".format(libras, euros))

else:
    print("Opción no válida. Si tienes otra divisa. ANDE A TOMAR POR CULO")