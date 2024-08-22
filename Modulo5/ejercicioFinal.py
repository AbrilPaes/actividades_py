import os

#1.Abrir el archivo capturado por usuario, incluyendo validación.
archivo = "carros" #input("Dame el nombre con extension del archivo: ")
archivo = archivo+".txt"

if os.path.exists(archivo):
    f=open(archivo, 'rt')
else:
    print("No se encontró el archivo")

#2. Abrir el archivo de carros.txt y crear el archivo para escribir resultados .txt
f2 = open('Resultados.txt','wt', encoding='utf-8')  

matriz=[]
encabezados = ['Marca','Modelo','Costo U.','IVA','Total']
matriz.append(encabezados)
#3. Ciclo para leer linea a linea el archivo carros
for renglon in f:
    """print(renglon)"""
    #4. Hacer los procesos para convertir cada renglon a la lista
    renglon=renglon.replace("\n"," ")
    producto=renglon.split(sep='\t')
    """print(producto)"""
    #5. Cada lista enviarla a una matriz
    matriz.append(producto)
"""print(*matriz,sep='\n')"""

#6 Tipos de datos correctos
#6.1 Obtener la antidad de filas y columnas de matriz
fil=len(matriz)
col=len(matriz[0])

#6.2 Proceso de correción de tipo de datos
for filas in range(1,fil):
    for c in range(col):
        if c>1:
            matriz[filas][c] = float(matriz[filas][c])               

#7. Buscar y contar productos
buscar = input("Dame la marca a buscar: ")
cont=0

for renglo in range(1,fil):
    if buscar in matriz[renglo]:
        cont+=1
        #print("Si encontro")
print(f'En la bd se encontraron {cont} productos de la marca {buscar}')  

#8. Cambiar marcas
marca1 = input("Cuál marca deseas cambiar: ")
marca2 = input("Cuál será el nuevo nombre de la marca: ")

for fi in range(1,fil):
    if c in range(col):
        if matriz[fi][0]==marca1:
            matriz[fi][0]=marca2
print(*matriz, sep="\n")
        
#9. Cambiar iva y total de cada producto
            
# Escribir la matriz final a un archivo resultados.txt
for renglon in range(fil):
    fila=matriz[renglon]
    f2.write(str(fila)+'\n')

f2.write(str(matriz))
f.close()
f2.close()