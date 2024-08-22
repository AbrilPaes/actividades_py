#Autor: Abril Pacheco Espinosa
"""
Escribe un programa que genere dos números aleatorios y despliegue en pantalla:
la suma, la resta, la multiplicación y la división de los mismos, la raíz cuadrada del
primer número y la potencia del primero por el segundo xy
Recuerda planear primero tu pseudocódigo y cuidar la documentación de tu código y
llamar a la librería al inicio del programa.

Entradas:num1,num2
Salidas:sum,resta,multi,div,raiz_num1,potencia_num2
Proceso:
1. Pedir entradas
2. Hacer operaciones y guardarlas en cada variable correspondiente.
3. Imprimir los resultados

Psudocódigo:
num1=randint()
num2=randint()

suma = num1+num2
resta = num1-num2
multi = num1*num2
div = num1//num2
raiz_num1 = num1**0.5
potencia_num2 = (num1)**num2

"""

from random import randint #numeros random enteros

#Presentación de programa
print("""Este programa simula una calculadora de suma, resta, multiplicación
división, raiz cuadrada y potencia con 2 números generados aleatoriamente"""
      )
#Entradas
num1 = randint(1,10)
num2 = randint(1,20)

#Proceso
suma = num1+num2
resta = num1-num2
multi = num1*num2
div = num1/num2
raiz_num1 = num1**0.5
potencia_num2 = (num1)**num2
potencia_xsegundo = (num1*num2)**2

#Impresión/Resultados
print("\n")
print(f"La suma de {num1}+{num2} es = {suma}" )
print(f"La resta de {num1}-{num2} es = {resta}")
print(f"La multiplicación de {num1}*{num2} es = {multi}")
print(f"La división entre {num1}/{num2} es = {div:.2}" )
print(f"La raiz cuadrada de {num1}**0.5 es= {raiz_num1:.2}")
print(f"La potencia del primer numero con el segundo {num1}**{num2} es = {potencia_num2}")
print(f"La potencia del primero por el segundo ({num1}*{num2})**2 es = {potencia_xsegundo}")
