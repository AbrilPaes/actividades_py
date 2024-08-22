m = [[3, 4, 4],[5, 2, 5],[9, 3, 2],[ 7, 10, 8]]

#Obtener la cantidad de filas y columnas
fil = len(m)
col = len(m[0])

print("Este código realiza la suma por filas \n")

#Crea el for de filas
for f in range(fil):
    suma=0
    #Crear el for de columnas
    for c in range(col):
        #Obtener el valor actual
        x=m[f][c]
        suma= suma+x
    print(f'La suma de la fila {f} es: {suma} ')
print(*m, sep="\n")

########################################################
########################################################

print("Este código realiza la suma por columnas \n")

#Crea el for de filas
for c in range(col):
    suma=0
    #Crear el for de columnas
    for f in range(fil):
        #Obtener el valor actual
        x=m[f][c]
        suma= suma+x
    print(f'La suma de la columna {c} es: {suma} ')
print(*m, sep="\n")

