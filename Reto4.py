#Autor: Abril Pacheco Espinosa

"""
Realiza un programa que convierta una medida en centimetros a pies, pulgadas y
yardas. El programa recibe la cantidad de centímetros y muestra a pantalla su
equivalente en pies, pulgadas y yardas

Entradas: medida
Salidas:medida_pies, medida_pulgadas, medida_yarda
Proceso:
1. Pedir entrada (medida a convertir)
2. Convertir la medida en cm a pies, pulgadas y yardas correspondientes.
3. Guardar las conversiones en variables.
4. Imprimir los resultados

Psudocódigo:

medida = float(input())
medida_pies = medida/30.48
medida_pulgadas = medida/2.54
medida_yardas = medida/91.44

print("Resultado",medida_pies, medida_pulgadas, medida_yarda )

"""

print("""Este programa permitirá al usuario ingresar una medida en centímetros
         y mostrar la conversión en pies, pulgadas y yardas.
""")

medida = float(input("Ingresa la medida en cm a convertir: "))
medida_pies = medida/30.48
medida_pulgadas = medida/2.54
medida_yardas = medida/91.44

print(f"""\n{medida:.2f} centímetros es igual a : \n
\t {medida_pies:.2f} pies.
\t {medida_pulgadas:.2f} pulgadas.
\t {medida_yardas:.2f} yardas"

""")
