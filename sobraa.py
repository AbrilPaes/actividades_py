"""
Una fárica de lápices te pidió que diseñes un programa para que,
no importando la cantidad de lápices producidos al día, se empaqueten
completamente en cajas de 80,50 y 20.

"""

print("este programa calcula las cajas de lapices empacadas en un dia, cajas de 80, 50 y 20 ")
#entradas
lapices = int(input("cuantos lapices se fabricaron hoy: "))
#proceso
caja80 =lapices //80
sobra = lapices % 80
caja50 = sobra // 50
sobra50 = sobra % 50
caja20 = sobra50 // 20
sobrante= sobra50 % 20

print(f"""
para la cantidad de {lapices} producidos hoy se generaron:
cajas empacadas de 80 piezas fueron: \t {caja80}
cajas empacadas de 50 piezas fueron: \t {caja50}
cajas empacadas de 20 piezas fueron: \t {caja20}
y los lapices que sobraron fueron: \t {sobrante}""")