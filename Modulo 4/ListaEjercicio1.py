import random

#Genera una lista de 10 elementos con números random

primerLista = [] #lista vacia
n=10 #tamaño de lista

for i in range (n): #inicio, fin, salto
    x=random.randint(1,20) #desde, hasta
    primerLista.append(x)
    
print(primerLista)

#Encuentra cuál es el número máximo generado
maximo = max(primerLista)
print(maximo)

#Encuentra cuál es el número mínimo generado
minimo = min(primerLista)
print(minimo)

#Copia la primera lista a otra lista
copiaLista = primerLista.copy()
print(copiaLista)

#Ordena la primera lista a otra lista
copiaLista.sort(reverse=True) 
print(copiaLista)


#De la lista ordenada, suma los elementos que se encuentran en las
#posiciones pares.

suma=0
for i in range(0,n,2):
    x = copiaLista[i] #obtener el valor de la lista en posicion 1
    print(copiaLista[i])
    suma=suma+x
print(f"suma de posiciones pares: {suma}")      

#De la lista ordenada suma todos los números impares.

suma2=0
print("entrando a for")
print(copiaLista)
for valor in (copiaLista):
    #print(i)
    if valor%2==1:
        suma2=suma2+valor
        print(f"impar: {valor}")
print(f"suma impar: {suma2}")
    

