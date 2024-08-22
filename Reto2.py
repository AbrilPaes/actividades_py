#Autor: Abril Pacheco Espinosa

"""
En una tienda departamental, es temporada de descuentos. Realiza un programa que
facilite conocer cuánto es el precio total del producto ya aplicado el descuento. De
manera que, tu programa deberá recibir, el precio sin descuento del producto y el
porcentaje que tiene de descuento. El resultado deberá ser, el monto a pagar después
de aplicar el descuento.

Entradas:precioProducto, porcentajeDescuento
Salidas:montoPagar
Proceso:
1. Pedir entradas, costo del producto y descuento que tiene
2. Hacer operaciones, (calcular monto de descuento y restarlo al precio de producto)
3. Guardar resultado en la variable montoPagar.
4. Imprimir resultado

Pseudocódigo:
precioProducto = input()
porcentajeDescuento = input()
montoPagar = precioProducto-((precioProducto)*(porcentajeDescuento*0.01))

"""

#Presentación de programa
print("Este programa calcula el monto total de un producto con porcentaje de descuento ya aplicado \n" )


#Pedir entradas
precioProducto = float(input("Ingresa el precio del producto: "))
porcentajeDescuento = float(input("Ingresa el descuento que tiene: "))

#Proceso/Cálculos
convertirDescuento = porcentajeDescuento*0.01
montoPagar = precioProducto-((precioProducto)*(porcentajeDescuento*0.01))

#Impresión de resultado
print(f"El {porcentajeDescuento}% del producto con precio de ${precioProducto:.2f} es ${(precioProducto)*(porcentajeDescuento*0.01):.2f} ")
print(f"El monto total a pagar del articulo con precio inicial de ${precioProducto:.2f} será de ${montoPagar:.2f}")