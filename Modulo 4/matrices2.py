#Importación de librerias
import random

#1 Obtener la cantidad de filas y columnas
fil = int(input("Dame la cantidad de filas: "))
col = int(input("Dame la cantidad de columnas: "))

#2 Crear la matriz vacia
matriz = []
#3 for para filas
for f in range(fil):
    #4 Crear una fila auxiliar vacia
    lista=[]    
    #5 for para columnas
    for c in range(col):
        #6 crear el valor
        valor = random.randint(1,10)
        #7 Se agrega a la lista
        lista.append(valor)    
    #8 La lista se agrega a la matriz
    matriz.append(lista)
    print(lista)
print(matriz)
print(*matriz,sep='\n')#impresion con formato o empaquetado 