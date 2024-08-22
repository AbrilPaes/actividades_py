import os
#1 Abrir archivo capturado por usuario, incluyendo validación
archivo="carros"#input("Dame el nombre del archivo: ") #carros.txt
archivo=archivo+".txt"

if os.path.exists(archivo):
    f=open(archivo,'rt') #leer el archivo fuente
else:
    print("no se encontró el archivo")

#2 abrir el archivo de carros.txt y crear archivo para escribir resultados.txt
f2=open("Resultados.txt",'wt') #archivo resultados para almacenar el resultado

m=[]
encabezados=['Marca','Modelo','Costo U.','IVA','Total']
m.append(encabezados) #agregamos el encabezado
#3 Ciclo para leer linea a linea el archivo carros
for renglon in f:
    #4 Hacer los procesos para convertir cada renglon a lista
    renglon=renglon.replace("\n","")#quitando los saltos de línea
    producto=renglon.split(sep='\t') #converir el string a lista
    #5 cada lista enviarla a una matriz
    m.append(producto) #agregamos la lista a la matriz


#6Tipos de datos correctos
#6.1 obtener la cantidad de filas y columnas de m
fil=len(m)#Cantidad de filas/renglones
col=len(m[0])#Cantidad de columnas
#6.2Proceso de corrección de tipo de datos
for fi in range(1,fil):
    for c in range(col):
        if c>=2:
            m[fi][c]=float(m[fi][c])#convertimos el tipo de dato a string
     
        
#7 buscar y contar productos
buscar=input("Dame la marca a buscar: ")
cont=0
for ren in range (1,fil):
    if buscar in m[ren]:
        cont+=1
print(f'En la BD se encontraron {cont} productos de la marca {buscar}')   

#8 cambiar marcas
marca1=input("Cuál marca deseas cambiar: ")
marca2=input("Cuál sera el nuevo nombre de la marca: ")
for fi in range (1,fil):
    for c in range(col):
        if m[fi][0]==marca1: #busca si la fila encuentra la marca buscada
            m[fi][0]=marca2 #realiza el cambio de marca


# Escribir la matriz final a un archivo resultados.txt
for renglon in range(fil):
    f2.write(str(m[renglon])+'\n') #se escribe cada renglon en la matriz

f.close()#carros
f2.close()#Resultados
