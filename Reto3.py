#Autor: Abril Pacheco Espinosa
"""
En una tienda departamental, es temporada de descuentos. Realiza un programa que
facilite conocer cuánto es el precio total del producto ya aplicado el descuento. De
manera que, tu programa deberá recibir, el precio sin descuento del producto y el
porcentaje que tiene de descuento. El resultado deberá ser, el monto a pagar después
de aplicar el descuento. Modifica la copia para que pueda funcionar para la
segunda fase de la temporada de descuento, es esta segunda temporada, los precios
tienen dos descuentos

Entradas:precioProducto, porcentajeDescuento,porcentajeDescuento2
Salidas:montoPagar
Proceso:
1. Pedir entradas, costo del producto, primer descuento, segundo descuento
2. Hacer operaciones para calcular ambos descuentos y guardarlos en variables.
3. Guardar resultado en la variable montoPagar.
4. Imprimir resultado

Pseudocódigo:
precioProducto = float(input())
porcentajeDescuento = int(input())
convertirDesc1 = porcentajeDescuento*0.01
descuento1 = precioProducto-(precioProducto * convertirDesc1)

porcentajeDescuento2 = int(input())
convertirDesc2 = porcentajeDescuento2*0.01
montoPagar = descuento1-(descuento1*convertirDesc2)

"""
#Presentación de programa
print("Este programa calcula el monto total de un producto con 2 porcentajes de descuentos ya aplicado \n" )


#Pedir entradas
precioProducto = float(input("Ingresa el precio del producto: "))
porcentajeDescuento = int(input("Ingresa el primer descuento que tiene: "))

#Proceso/Cálculos
convertirDesc1 = porcentajeDescuento*0.01
descuento1 = precioProducto-(precioProducto * convertirDesc1)

porcentajeDescuento2 = int(input("Ingresa el segundo descuento que tiene: "))
convertirDesc2 = porcentajeDescuento2*0.01
montoPagar = descuento1-(descuento1*convertirDesc2)

#Impresión de resultado

print(f"""El monto total del producto con precio original de ${precioProducto:} y con descuentos de {porcentajeDescuento}%
y {(porcentajeDescuento2)}% es de: ${montoPagar:.2f} """)
