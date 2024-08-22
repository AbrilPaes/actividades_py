
suma=0
cont=1

alumnos = int(input(f"Cantidad de alumnos: "))

while cont<=alumnos:
    cal = float(input(f"Escribe las calificaciones: "))
    suma = suma+cal
    cont = cont+1
    promedio=suma/8
    
print(f"El promedio es de {promedio:.2f}")