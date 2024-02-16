miLista=[1,2,3]
opcion=0
while opcion!=4:
    print(".......MENU......")
    print("1.-Agregar Elemento")
    print("2.-Borrar Elemento")
    print ("3.- Mostrar lista")
    print("4.- Salir")
    opcion=int(input("Ingresa la opcion:"))

    match opcion:
        case 1:
            print("-----------------------")
            print("Agregar Elemento")
            print("-----------------------")
            el=input("Ingresa el elemento")
            miLista.append(el)

        case 2:
            print("-----------------------")
            print("Borrar Elemento")
            print("-----------------------")
            cont=1
            for c in miLista:
                print("La posicion", c, "es:",cont)
                cont=cont+1
            pos= int(input("Ingresa la posicion "))
            miLista.pop(pos)

        case 3:
            print("-----------------------")
            print("Borrar Elemento")
            print("-----------------------")
            print (miLista)


        case 4:
            print("-----------------------")
            print("Saliendo")
            print("-----------------------")

        case 5:
            print("-----------------------")
            print("La opcion no es valida")
            print("-----------------------")




