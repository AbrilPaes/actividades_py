"""
Una tienda mayorista de focos vende únicamente 3 productos, foco alógeno
luz cálida $250 pesos la caja con 10 piezas, foco ahorrador 9w $ 700.00
pesos la caja con 10 piezas y foco ahorrador circular 32 w, $1000 pesos
la caja con 10 piezas. 
Dependiendo del monto del pedido, la tienda ofrece facilidades de pago
de acuerdo con los siguientes rangos. 
Si el cliente compró hasta $5,000, el pago será en una sola exibición.
Si compró más de $5000 pero menos de $30000, el pago podrá realizarse a
3 meses sin intereses, si compró más de 30000 podrá elegir pago en una sóla
exibición con un 5% de descuento ó un pago a 9 meses sin intereses. 
Tu programa deberá preguntar cuántas cajas de cada producto desea el cliente,
presentar el monto de compra, plantear las opciones de pago,
y presentar el pago elegido con el monto a pagar
(en el caso de meses sin intereses o con el 5% de descuento)

"""
#Presentar programa
print("Este programa te indica el total de tu compra así como las opciones de pago de acuerdo a la cantidad comprada. ")

#Pedir entradas
fc_alog = int(input("Ingresa la cantida de foco alógeno luz cálida : "))
fc_ahorro9w = int(input("Ingresa la cantida de foco ahorrador 9w : "))
fc_ahorro32w = int(input("Ingresa la cantidad de foco ahorrador circular 32w : "))
#Hacer operaciones 
pagoT= ( (fc_alog*250) + (fc_ahorro9w*700) + (fc_ahorro32w*1000) )


#Resultados impresos

print(f"El total de tu compra fue de ${pagoT:.2f}")

if pagoT <=0:
    print("No has comprado nada, por lo que no se puede aplicar ningún tipo de opción o facilidad de pago.")
elif pagoT<=5000:
    print(f"El pago será en una sola exibición ${pagoT:.2f}")
elif pagoT<=30000:
    mensualidad = pagoT/3
    print(f"El pago puede ser a 3 meses sin intereses de ${mensualidad:.2f} cada mes.")
else:
    descuento = pagoT-(pagoT*0.05)
    mensualidad = pagoT/9
    print(f"""El pago puede hacerse en una sóla exibición con un 5% de descuento con total de: ${descuento:.2f}
            ó un pago a 9 meses sin intereses pagando ${mensualidad:.2f} cada mes.""")






