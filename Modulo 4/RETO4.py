#Autor: Abril Pacheco Espinosa

"""
Este programa presenta la resolución del Reto Módulo 4.
Listas de listas con funciones.

"""


def llenarLista():
    lista=[]
    
    cantidad=int(input("¿Cuántos valores quieres en tu lista?: "))
    
    for i in range (1,cantidad+1): #inicio, fin, salto
        valor=int(input(f"Dame el valor {i}: "))
        lista.append(valor)
    return lista

def contabilizar(lista):
    contarValor=0
    for valor in lista:
        if valor>15:
            contarValor = contarValor+1
    return contarValor

def promedioLista(lista):
    suma=0
    promedio=0
    
    for i in lista:
        suma=suma+i 
    promedio = suma/len(lista)
    return promedio

def cambioIndice(lista):
    
    pos=int(input("Dame la posición: "))
    if pos >= 0 and pos < len(lista):
        num=int(input("Dame nuevo valor: "))
        lista[pos] = num
        print("\nLa lista se ha modificado.")
    else:
        print("\n||¡No existe ese índice en la lista.!||")
    return lista

def cambioValor(lista):
    buscar=int(input("Dame un valor a reemplazar: "))
    
    if buscar in lista:
        numNuevo=int(input("Dame el nuevo valor: "))
        
        for i in range(len(lista)):
            if lista[i] == buscar: #obtener el valor de la lista en posicio
                lista[i] = numNuevo
        print(f"Valor {buscar} reemplazado con {numNuevo}.\nLista: {lista}")
    else:
        print("No hay ningún número igual al que desea reemplazar.")
      
def eliminarValor(lista):
    num=int(input("Dame el valor a eliminar: "))
    pos=int(input("Dame su posición: "))
    
    if pos >= 0 and pos < len(lista):
        if lista[pos] == num:
            del lista[pos]
            print("Elemento eliminado. Lista actualizada:", lista)
        else:
            print("El valor en la posición no coincide con el valor.")
    else:
        print("La posición proporcionada está fuera de rango.")

def texto():
    txt = "La vida es un lienzo en blanco, y cada día es una pincelada de nuestras elecciones. Con cada trazo, creamos la obra maestra de nuestro destino."
    return txt

def contarVocales():
    cadena = input("Ingresa una cadena para contabilizar sus vocales: ")
    txt= cadena.lower()
    a = txt.count('a')
    e = txt.count('e')
    i = txt.count('i')
    o = txt.count('o')
    u = txt.count('u')
    return a, e, i, o, u
    

def encontrarP(msg):
    buscar= input("Ingresa la palabra a buscar en el texto establecido por mi: ")
    minus = msg.lower()
    palabra= minus.split()

    print(f"\n{msg}")
    if buscar.lower() in palabra:
        print(f"\nSí, la palabra {buscar} se encuentra en el texto.")
    else:
        print(f"\nOps, la palabra {buscar} NO se encuentra en el texto.")

def convertirCadena():
    cadena = input("Ingresa una cadena para convertir a lista: ")
    listaCadena = list(cadena)
    print(f"Tu string: {cadena} ")
    print(f"Tu string convertido a lista: {listaCadena} ")

def cifrado():
    cadena = input("Ingresa una cadena para cifrar: ")    
    cadenaCod = cadena.replace('a', '3').replace('e', '5').replace('i', '8').replace('o', '9').replace('u', '2')    
    return cadena,cadenaCod

print(f"""Este programa presenta un menú con las opciones
que se pueden realizar utilizando listas y strings. \n""")

while True:
    
    print("""
    .--.--.--.--.--.--.--.--.--.--.--.--.--.
               String y Listas
                   M E N Ú  
    .--.--.--.--.--.--.--.--.--.--.--.--.--.
             1. Llenar lista vacia
             2. Contar valores >15
             3. Promedio de valores 
             4. Cambiar valor
             5. Eliminar valor
             6. Crear texto
             7. Contar vocales
             8. Encontrar palabra
             9. Convertir string a lista
             10. Cifrado de cadena
             11. SALIR """)
    
    menu = int(input("Elige una opción del menú: "))
    
    if menu==1:
        print()
        listaLlena = llenarLista()
        #copiaLista = listaLlena.copy()
        print(listaLlena)
    elif menu==2:
        print()
        contadorVal = contabilizar(listaLlena)
        print(f"Los valores mayores a 15 son {contadorVal}")
    elif menu==3:
        print()
        prom = promedioLista(listaLlena)
        print(f"El promedio de la lista es de: {prom} ")
    elif menu==4:
        print()##Submenú de cambio de valor
        print("""\t\t\t  S u b m e n ú -Cambio de valor-
                    1. Por índice
                    2. Por valor""")
        opcion = int(input("Elige una opcion: "))
   
        if opcion==1:
            print("=Cambio de valor por índice=")
            modifica=cambioIndice(listaLlena)
            print(f"Contenido de la lista: {modifica}")
            
        elif opcion==2:
            print("=Cambio de valor por valor=")
            cambioValor(listaLlena)
            
        else:
            print("Opción no válida.")#Termina submenú de cambio de valor      
                
    elif menu==5:
        print()
        eliminarValor(listaLlena)
    elif menu==6:
        print()
        msg=texto()
        print(f"El texto creado es: {msg}")
    elif menu==7:
        print()
        ca, ce, ci, co,cu = contarVocales()
        print(f"""Contador de vocales:\n
 a: {ca}\n e: {ce}\n i: {ci}\n o: {co}\n u: {cu} """)
    elif menu==8:
        print()
        msg=texto()
        encontrarP(msg)
    elif menu==9:
        print()
        convertirCadena()
    elif menu==10:
        print()
        cade,codificado=cifrado()
        print(f"Tu texto fue: {cade}")
        print(f"Tu texto cifrado es: {codificado}")
        
    elif menu==11:
        print("Saliendo...")
        break
    
    else:
        print("Opcion no existente.")
    
    