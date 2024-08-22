
suma=0
dias=1

while dias<=7:
    cantidad = int(input(f"Dame la cantidad de venta del día {dias}: "))
    suma = suma+cantidad
    dias=dias+1
    
print(f"El total de la venta en {cantidad} días es de ${suma:.2f}")