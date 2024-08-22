"""
Escribe un programa que identifique si un número es par o impar.

Entrada: num
Proceso: dividido el numero con mod2...
         si el resultado es 0,
         entonces el número es par,
         sino
         entonces el número es impar
Salida: mensaje de si es par o impar

"""

print("Este programa identifica si un número es par o impar.")

num = int(input("Dame un número: "))
if num%2 == 0:
    print(f"{num} es par.")
else:
    print(f"{num} es impar.")





