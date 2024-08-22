"""

Si la calificación tanto del examen como del proyecto es mayor o igual a 80
despliega la palabra
APROBADO, Si la calificación del examen es mayor a 70 y
del proyecto mayor a 50 despliega,
CONDICIONADO, en caso contrario la palabra mostrada es REPROBADO

"""

print("Este programa determina si estás aprobado, condicionado o reprobado. ")

cal_exam = int(input("Ingresa la calificación de tu examen: "))
cal_proye = int(input("Ingresa la calificación: "))

if cal_exam >= 80 and cal_proye >= 80:
    print("¡Aprobado!")
elif cal_exam > 70 and cal_proye > 50:
     print("¡Condicionado! ")
else:
    print("Reprobado :c ")



