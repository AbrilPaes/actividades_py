"""
Este programa simula una calculadora.

Entradas: num1,num2
Salidas: res_suma, res_resta, res_multi
Proceso:

1.Pedir las entradas.
2. Hacer operaciones y guardar los resultados en las variables de salida
3. Presentar los resultados

Pseudocódigo
num1=input()
num2=input()
res_suma = num1+num2
res_resta = num1-num2
res_multi = num1*num2
print(res_suma)
print(res_resta)
print(res_multi)
"""

from random import randint #randint es una funcion que genera numeros random enteros
print("Este programa simula una calculadora de suma, resta y multiplicación ")
#Entradas
num1 = randint(1,200)
num2 = randint(1,100)

#Proceso
res_suma = num1+num2
res_resta = num1-num2
res_multi = num1*num2

#Salida
print(f"{num1}+{num2} = {res_suma}" )
print(f"{num1}-{num2} = {res_resta}")
print(f"{num1}*{num2} = {res_multi}")

"""
num1 = int(input("Dame un número: "))
#genera un número aleatorio entre 1 y
rango
num2 = int(input("Dame otro número: "))
while num2==0:
#se queda ciclado mientras num2 sea 0
print("Error de división entre 0")
num2=int(input("Dame un número diferente de 0 para la división "))

division=num1 / num2
print(f"{num1}/{num2} = {division:.2f}\n")

"""


