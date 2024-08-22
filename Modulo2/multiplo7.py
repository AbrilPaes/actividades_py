"""
Escribe un programa que identifique si un número es múltiplo de 7

Entrada: num
Proceso: dividido el numero con mod7...
         si el resultado es 0,
         entonces el número es multiplo de 7,
         sino
         entonces el número no es multiplo de 7
Salida: mensaje de si es múltiplo o no

"""

print("Este programa identifica si un número es múltiplo de 7.")

num = int(input("Dame un número: "))
if num%7 == 0:
    print(f"{num} es múltiplo de 7.")
else:
    print(f"{num} es no múltiplo de 7.")
