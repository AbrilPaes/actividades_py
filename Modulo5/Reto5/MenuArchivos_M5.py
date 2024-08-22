#Autor: Abril Pacheco Espinosa
#Fecha: 07 de Abril del 2024

"""
Entregable Particas Módulo 5
RETO módulo 5. Programando con Python
Menú de archivos

"""


def mostrarContenido():
    # Abre el archivo en modo lectura
    contenido=open('mascotas.txt','rt', encoding='utf-8')
    print(contenido.read())
    contenido.close()

def archivoLinea():
    contenido=open('mascotas.txt','rt', encoding='utf-8')
    for i in contenido:
        print(i,"\n")
    contenido.close()

def buscar_palabra(palabra):
    matriz = []
    contenido = open('mascotas.txt', 'rt', encoding='utf-8')
    for linea in contenido:
        fila = linea.strip().split(',')
        matriz.append(fila)

    encontrada = False
    for fila in matriz:
        if palabra in fila:
            encontrada = True
            break

    if encontrada:
        print("La palabra '" + palabra + "' se encontró en el archivo.")
    else:
        print("La palabra '" + palabra + "' no se encontró en el archivo.")
    contenido.close()


def agregar():
    matriz = []
    for campo in ['Tipo', 'Nombre', 'Raza', 'Género', 'Color', 'Comportamiento', 'Dueño']:
        valor = input(f"Ingrese {campo}: ")
        matriz.append(valor)
    
    contenido = open('mascotas.txt', 'a', encoding='utf-8')
    for elemento in matriz:
        contenido.write(str(elemento) + ',')
    contenido.write('\n')
    print(*matriz, sep=',')
    contenido.close()


def renglones():
    matriz = []
    contenido = open('mascotas.txt', 'rt', encoding='utf-8')
    renglon = 1
    primer_iteracion = True
    for linea in contenido:
        if primer_iteracion:
            nid=['ID','Tipo','Nombre','Raza','Género','Color','Comportamiento','Dueño']
            matriz.append(nid)
            primer_iteracion = False
        else:
            fila = [renglon] + linea.strip().split(',')  # Agrega número 
            matriz.append(fila)
            renglon += 1
    contenido.close()  # cierra archivo 
    
    contenido = open('mascotas.txt', 'w', encoding='utf-8')
    for fila in matriz:
        for i, elemento in enumerate(fila):
            contenido.write(str(elemento))
            if i != len(fila) - 1: 
                contenido.write(',')
        contenido.write('\n')
    contenido.close() # cierra archivo    
    return matriz

   
def convertir():
    matriz = []
    contenido = open('mascotas.txt', 'rt', encoding='utf-8')
    for linea in contenido:
        fila = linea.strip().split(',')
        matriz.append(fila)
    contenido.close()
    
    print(*matriz, sep='\n')
    
    return matriz


def eliminar():
    numero_linea = input("Ingrese el número de línea del registro que desea eliminar: ")
    matriz = convertir()  
    
    encontrado = False
    for fila in matriz:
        if fila[0] == numero_linea:
            matriz.remove(fila)
            encontrado = True
            break
    
    if encontrado:
        contenido = open('mascotas.txt', 'w', encoding='utf-8')

        for fila in matriz:
            for i, elemento in enumerate(fila):
                contenido.write(elemento)
                if i != len(fila) - 1:
                    contenido.write(',')
            contenido.write('\n')
        print("Registro eliminado correctamente.")
    else:
        print("El número de línea no se encontró en el archivo.")
    contenido.close()


print("El siguiente programa muestra un menú de archivos.\n")
print("""||Nota: Para realizar la opción 7, deberás haber seleccionado
primero la 6 para convertir a matriz.||""")
        
        
while True:
    print("""
    .--.--.--.--.--.--.--.--.--.--.--.--.--.
              F u n c i o n e s 
                   M E N Ú
    .--.--.--.--.--.--.--.--.--.--.--.--.--.
             
    1.Mostrar el contenido de un archivo
    2.Mostrar el contenido de un archivo línea a línea 
    3.Buscar elementos o palabras en el archivo 
    4.Escribir datos en archivo existente
    5.Agregar número del renglón a cada renglón 
    6.Pasar el archivo a lista de listas (matriz) 
    7.Eliminar por ID 
    8.SALIR """)
    
    menu = int(input("Elige una opción del menú: "))

    if menu == 1: 
        print()
        mostrarContenido()

    elif menu == 2:
        print()
        archivoLinea()

    elif menu == 3:
        print()
        palabra = input("Ingrese la palabra a buscar: ")
        buscar_palabra(palabra)

    elif menu == 4:
        print()
        agregar()
        mostrarContenido()

    elif menu == 5:
        print()
        matriz= renglones()  
        for fila in matriz:
            print(fila)

    elif menu == 6:
        print()
        convertir()

    elif menu == 7:
        print()
        eliminar()
        mostrarContenido()

    elif menu == 8:
        print("Saliendo")
        break

    else:
        print("Elige una opción existente (1-8)")