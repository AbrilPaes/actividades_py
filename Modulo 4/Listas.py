"""import random

valores = ['hola',123,True,3.1416]
print(valores)

print(valores[-1])

lista=[]

for i in range(1000000):
    x=random.randint(1,50)
    lista.append(x)

print(len(lista))

"""

"""
lista=['python','c']
num=int(input("Dame un valor: "))
pos=int(input("Dame la posición: "))
lista.insert(pos,num) #lista.append('Matlab')

print(lista)
"""
lista2=['python','c','python','Java','.Net',""]
#num=int(input("Dame un valor: "))
#pos=int(input("Dame la posición: "))
#lista2.insert((len(lista2))-1,num) #lista.append('Matlab')

print(lista2)

lista2.remove('python')#solo eliminará el primero que encuentre
print(f"se elimina 'python' {lista2}")

#Eliminar
print(f"se eliminará {lista2[2]}")
lista2.pop(2) #Colocar el indice lo elimina, o no colocarlo eliminará elúltimo

#del lista ... Elimina indice especificado o la lista completa.
print(lista2)


#Metodo Sort

lista2.sort() #Ordena la lista de forma ascendente.
print(lista2)

lista2.sort(reverse=True)#Ordena la lista de forma descendente.
print(lista2)


lista2.clear() #Elimina todos los elementos, deja la lista vacia
print(lista2)

#copiar listas
listaCopia = lista2.copy()
listaCopiaForma2 = list(lista2)

#contar cuantas veces aparece
num= x.count(5) #parametro cosa a buscar