print("ESTRUCTURAS DE SELECCION DE CALIFICACIONES")

cal = float(input("Dame una calificacion:"))

if cal == 100:
    print("EXCELENTE")

elif cal >= 90 and cal <= 99.9:
    print("MUY BIEN")

elif cal >= 80 and cal <= 89.9:
    print("BIEN")

elif cal >= 70 and cal <= 79.9:
    print("REGULAR")

elif cal >= 60 and cal <= 69.9:
    print("SUFICIENTE")


elif cal>=0 and cal<=60:
    print("REPROBADO")

else:
    print("Calificacion erronea")