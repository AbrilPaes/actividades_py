"""
Este programa indica si el usuario es mayor de edad

ENTRADA: edad
Salida: "eres mayor de edad" / "no eres mayor de edad"
Proceso: comparar la edad con 18,
si la edad es mayor o igual a 18,
    entonces es mayor de edad
    sino escribimos no eres mayor de edad

"""

print("Este programa indica si eres mayor de edad")
edad = int(input("Dime cuantos años tienes: "))
if edad>=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad :c ")
