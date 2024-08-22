"""
En una universidad cada estudiante cursa
4 materias en el semestre.
Desarrolla un programa que reciba
la calificación de cada materia,
calcula el promedio de las 4 materias
y lo despliegan

Entradas: calif1, calif2, calif3, calif4
Salidas: Promedio de materias
Proceso en español:
1.Pedir las 4 entradas
2. Sumar las 4 calificaciones
3. Dividir entre 4 la suma
4. Presentar resultado

Pseudocódigo:
materia1 = input()
materia2 = input()
materia3 = input()
materia4 = input()

suma = materia1+materia2+materia3+materia4
promedio= suma/4

"""

print("Este programa pide tus calificaciones de las 4 materias y presenta el promedio")
#Entradas
materia1 = float(input("Dame la calificación de la materia 01: "))
materia2 = float(input("Dame la calificación de la materia 02: "))
materia3 = float(input("Dame la calificación de la materia 03: "))
materia4 = float(input("Dame la calificación de la materia 04: "))

#Proceso
promedio =(materia1+materia2+materia3+materia4)/4

#Salida
print("El promedio de calificación de tus 4 materia es ", promedio)
