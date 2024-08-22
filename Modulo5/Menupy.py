#Inico de Menu
def menu():
    print("********    MENU    ********")
    print("Elige una de estas opciones \n"+"1.- Altas \n"+"2.- Bajas \n"+"3.- Modificacion \n"+"4.- Consulta \n"+"5.- Salir")

while True:
    menu()
    OP=(input("Introduce el numero de opcion > "))
#Incio de Altas
    if OP=="1":
        print ("")
        print("Has seleccionado Altas")
        print("Ingresa: \n")
        ID=input("ID: \n")
        Nom=input("Nombre: \n")
        Edad=input("Edad: \n")
        Sexo=input("Sexo: \n")
        print("Se han capturado: " + ID + "," + Nom + "," + Edad + "," + Sexo + ".")
        archivo = open("almacen.txt", "a")
        archivo.write(ID)
        archivo.write(",")
        archivo.write(Nom)
        archivo.write(",")
        archivo.write(Edad)
        archivo.write(",")
        archivo.write(Sexo)
        archivo.write("\n")
        archivo.close()
#Incio de Bajas
    elif OP=="2":
        import os
        print ("")
        print("Has seleccionado Bajas")
        Tmp=[]
        archivo = open("almacen.txt", "r")
        for linea in (archivo):
            Tmp.append(linea)
        archivo.close()
        archivo = open("almacen.txt", "w")
        Busqueda=input("Dame el ID: ")
        for linea in Tmp:
            if not Busqueda in linea:
                archivo.write(linea)
        archivo.close()
#Incio de Modificacion
    elif OP=="3":
        import os
        print ("")
        print("Has seleccionado Modificacion")
        Tmp=[]
        archivo = open("almacen.txt", "r")
        for linea in (archivo):
            Tmp.append(linea)
        archivo.close()
        archivo = open("almacen.txt", "w")
        Busqueda=input("Dame el ID: ")
        for linea in Tmp:
            if not Busqueda in linea:
                archivo.write(linea)
            else:
                print("Ingresa: \n")
                ID=input("ID: \n")
                Nom=input("Nombre: \n")
                Edad=input("Edad: \n")
                Sexo=input("Sexo: \n")
                archivo.write(ID)
                archivo.write(",")
                archivo.write(Nom)
                archivo.write(",")
                archivo.write(Edad)
                archivo.write(",")
                archivo.write(Sexo)
                archivo.write("\n")
        archivo.close()
#Incio de Consulta
    elif OP=="4":
        import os
        print ("")
        print("Has seleccionado Consulta")
        Tmp=[]
        archivo = open("almacen.txt", "r")
        for linea in (archivo):
            Tmp.append(linea)
        archivo.close()
        archivo = open("almacen.txt", "a")
        Busqueda=input("Dame el ID: ")
        for linea in Tmp:
            if not Busqueda in linea:
                archivo.write("")
            else:
              print(linea)
        archivo.close()
#Incio de Salida
    elif OP=="5":
        print ("")
        print("Has seleccionado Salir \nHasta la proxima (Dupsted) ;)")
        exit(0)
        break
    else:
        print ("")
        input("Por favor seleccione una opcion valida \nPresione cualquier una tecla para continuar")