diccionario={}
opcion=0
while opcion!=5:
    print(".......MENU......")
    print("1.-Agregar Elemento")
    print("2.-Modificar Elemento")
    print ("3.- Borrar elemento")
    print("4.- Mostrar Diccionario")
    print("5.- Salir")
    opcion=int(input("Ingresa la opcion:"))

    match opcion:
        case 1:
            print("-----------------------")
            print("Agregar Elemento")
            print("-----------------------")
            el1= input("Ingresa el elemento:")
            defi = input("Ingresa el elemento 2:")
            diccionario[el1]= defi

        case 2:
            print("-----------------------")
            print("Modificar Elemento")
            print("-----------------------")
            print(diccionario)
            el = input("Ingresa el elemento que deseas modificar:")
            ne = input("Ingresa la modificacion:")
            diccionario[el]=ne

        case 3:
            print("-----------------------")
            print("Borrar Elemento")
            print("-----------------------")
            print(diccionario)
            pos= input("Ingresa el elemento a borrar: ")
            diccionario.pop(pos)

        case 4:
            print("-----------------------")
            print("Imprimir Diccionario")
            print("-----------------------")
            print (diccionario)


        case 5:
            print("-----------------------")
            print("Saliendo")
            print("-----------------------")

        case 6:
            print("-----------------------")
            print("La opcion no es valida")
            print("-----------------------")
