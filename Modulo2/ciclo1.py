"""
En este progrma practicaremos ciclos simples
Estructura de un CICLO

while condición:
    todo lo que esté identado se estará ejecutando
    mientras la condición sea verdadera dentro del ciclo,
    algo debe pasarle a la variable de la condición para
    que llegue un momento en que, por el cambio,
    la condición sea falta y el ciclo termina.

"""

num = int(input("Dame de qué número quieres la serie numérica: "))
cont=num
while cont<100:
    print(cont, end= " ")
    cont = cont+num

print(f"Este ciclo se ejecutó {cont} veces.")



