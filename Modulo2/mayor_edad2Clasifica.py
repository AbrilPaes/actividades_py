"""
Este programa clasifica a la persona, dependiendo su edad.

0-3 años es un bebé
4-11 años: niños
12-17: adolescente
18-59: adulto
60 en adelante: adulto mayor

ENTRADA: edad
Salida: "Clasificacion de adulto: "
Proceso: 

"""
#Validación
print("Clasifica tu rango de edad. ")
edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Error")
elif edad < 4:
    print("Es un bebé. ")
elif edad < 12:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
elif edad < 60:
    print("Eres un adulto")
else: 
    print("Eres un adulto mayor")

    