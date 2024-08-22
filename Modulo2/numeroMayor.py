"""
Hacer un programa que pida dos números diferentes y despliegue el número
más grande.

"""

print("Este programa despliega el número más grande ")

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1>num2:
    print(f"El número más grande es {num1}")
else:
    print(f"El número más grande es {num2}")