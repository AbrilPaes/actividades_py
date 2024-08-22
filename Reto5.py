#Autor: Abril Pacheco Espinosa

"""
Escribe un programa que dada una cantidad en segundos, convierta a horas, minutos y
segundos restantes. (Utiliza DIV y MOD para resolver este reto y cuida que la entrada
sea entero, aquí no se formatean decimales porque no debe haber decimales).


Entradas: cantidad_seg
Salidas: cantidad_horas, cantidad_minutos, seg_restantes

Proceso:
1. Pedir la cantidad de segundos a convertir
2. Dividir la cantidad de segundos entre 3600 (equivalente a 1hr)
3. Recuperar el residuo y dividirlo entre 60 (equivalente a 1min)
4.Recuperar el residuo de la división (corresponde a los seg restantes)
3. Guardar las conversiones en variables.
4. Imprimir los resultados

Psudocódigo:
cantidad_seg = input()

cantidad_horas = cantidad_seg//3600
cantidad_seg = cantidad_seg%3600
cantidad_minutos = cantidad_seg//60
seg_restantes = cantidad_seg%60

"""
#Presentación de programa
print("""		Este programa calcula las hora/s, minutos y segundos restantes
                    convertidas dada una cantidad de segundos.\n """)

#Pedida de entrada
cantidad_seg = int(input("""Ingresa los segundos que quieres convertir: """))

#Proceso
cantidad_horas = cantidad_seg//3600 #obtengo las horas equivalentes
cantidad_seg = cantidad_seg%3600 #actualiza variable y recupera residuo
cantidad_minutos = cantidad_seg//60 #Divide entre 60seg = 1min
seg_restantes = cantidad_seg%60 #Resto = segundos restantes

#Impresión de resultado
print("\n")
print(cantidad_seg, " segundos son equivalentes a ", cantidad_horas," hora/s, ", cantidad_minutos, " minutos y ", seg_restantes, " segundos.")
