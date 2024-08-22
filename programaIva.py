"""
Este programa calcula el monto del IVA que se carga a un producto
o servicio.
El IVA No es una entrada del programa

Entradas: costo
Salidas: iva
Proceso:
1. Decirle al usuario de qué se trata el programa
2. Pedirle el costo del producto o servicio y guardarlo en la
variable
3. Calcular el iva (México: multiplicar cotso *.16 y guardarlo en l a variable iva;
  Costa Rica: multiplicar el costo*0.13 y guardarlo en la variable iva)
4. Presentar el resultado

"""

print("""
        Este programa está diseñado para:
        Calcular el iva de un servicio
        Calcular el pago total
        Practicar programación
        """)


precioSinIva = float(input("\t Dame el precio del articulo: "))
iva = precioSinIva*.16
pagoConIva = iva + precioSinIva
print(f"Tu iva es \t${iva:.2f}")
print(f"Precio final \t${(iva + precioSinIva):.2f}")

