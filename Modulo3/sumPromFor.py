suma=0 #Se inicializó en 0

for num in range(1,6):
    suma=suma+num #acumulador

promedio =suma/num
print(f"La suma de los números del 1 al 5 es: {suma}")
print(f"El promedio de los npumeros del 1 del 5 es: {promedio:.2f}")

print("\n" )  
for i in range(2,6):
    print(i, i*i, i+i)

suma2=0
for i in range (1,8):
    ganancia=float(input(f"Escribe la cantidad vendida en el día {i}: "))
    suma2=suma2+ganancia
print(suma2)

