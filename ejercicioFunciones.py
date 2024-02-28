
def grafar(z):
    b=(9/5)
    c=32
    gf=(z*b)+c
    return gf

def numpn(a):
    r=''
    if a>0:
        print ("El numero es positivo")
    else:
        print ("El numero es negativo")
    return r

def parimp(z):
    c=2
    r=''
    if z%c==0:
        print ("El numero es par")
    else:
        print("El numero es impar")
    return r

def suma(a,b,c,d,e):
    s= a+b+c+d+e
    return s

def numlet(a):
    r=''
    if z==1:
        print("UNO")
    if z==2:
        print("DOS")
    if z==3:
        print("TRES")
    if z==4:
        print("CUATRO")
    if z==5:
        print("CINCO")
    if z==6:
        print("SEIS")
    if z==7:
        print("SIETE")
    if z==8:
        print("OCHO")
    if z==9:
        print("NUEVE")
    if z==10:
        print("DIEZ")
    return r

opcion=0
while opcion!=6:
    print(".......MENU......")
    print("1.-Convertir de centigrados a fahrenheit")
    print("2.-Numero positivo o negativo")
    print ("3.- Numero par o impar")
    print("4.- Covertir numero a letra(1-10)")
    print("5.- Lista de 5 numeros a suma")
    print("6.- Salir")

    opcion=int(input("Ingresa la opcion:"))

    match opcion:
        case 1:
            print("Convertir de centigrados a fahrenheit")
            c=int(input("Ingresa grados centigrados:"))
            a=grafar(c)
            print(c, "grados centigrados es igual a : ", a, "grados Fahrenheit")


        case 2:
            print("Numero positivo o negativo")
            print("-----------------------")
            a= int(input("Ingresa un Numero:"))
            z=numpn(a)
            print(z)

        case 3:
            print("Numero par o impar")
            print("-----------------------")
            z=int(input("Ingresa un numero:"))
            a=parimp(z)
            print(a)

        case 4:
            print("Covertir numero a letra(1-10)")
            print("-----------------------")
            z= int(input("Ingresa un Numero del 1 al 10: "))
            b= numlet(z)
            print(b)

        case 5:
            print("Lista de 5 numeros a suma")
            print("-----------------------")
            a = int(input("Dame a:"))
            b = int(input("Dame b:"))
            c = int(input("Dame c:"))
            d = int(input("Dame d:"))
            e= int(input("Dame e:"))
            z=suma(a,b,c,d,e)
            print("La suma es: ", z)

        case 6:
            print("Salir")
