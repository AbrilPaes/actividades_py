"""
El programa te pregunta cuánto dinero tienes en ahorros y a cuánto
ascienden tus gastos.
Si los ahorros son mayores a los gastos, se deberá desplegar
la palabra SOLVENTE. En
caso contrario se despliega el texto EN QUIEBRA

"""

print("Este programa determina si estás en quiebra o no de acuerdo a tus ahorros. ")

ingreso = float(input("¿Cuánto dinero tienes en ahorros?: "))
gastos = float(input("¿A cuánto ascienden tus gastos?: "))

if ingreso>gastos:
    print("SOLVENTE ")
else:
    print("EN QUIEBRA ")
    