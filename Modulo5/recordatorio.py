import random
#1 Obtener la cantidad de filas y columnas

fil = int(input("Dame la cantidad de filas: "))
col = int(input("Dame la cantidad de columnas: "))

#Crear la matriz vacía
m = []

#3 crea el for de filas
for f in range (fil):
    #4 Crear una fila vacia
    fila = []
    #5 Crear el for de columnas
    for c in range(col):
        #6 Crear el valor
        x = random.randint(1,10)
        #Agregar el valor x a la fila
        fila.append(x)
    #agregar la fila a la matriz
    m.append(fila)

print(*m, sep = "\n")