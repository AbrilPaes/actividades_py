#Autor: Abril Pacheco Espinosa
#Fecha: 08 de Marzo del 2024

"""
FUNCIONES y Estructuras de control cíclicas –for & while
Programando con Python
RETO módulo 3. Programando con Python

Este programa permite a los niños a practicar el cálculo mental.
Tiene un menú para elegir entre las opciones como: suma, resta, multiplicación
y salir del programa. 
"""
from random import randint #números random

# Juego de Sumas
def sumaNivelDos():
    print("Segundo nivel. ¡Eres muy buen@ eeh, diviertéte! ")
    intentosCorrectos=0
    intentosIncorrectos=0
    
    for i in range(5):
        num1 = int(randint(1,9))
        num2 = int(randint(10,100))
        respUsuario= int(input(f"¿Cuánto es {num1} + {num2}? "))
        suma = num1+num2
        
        if respUsuario == suma:
            print("Woow Respuesta correcta!!")
            intentosCorrectos = intentosCorrectos+1
        else:
            print("Nono, Respuesta incorrecta")
            intentosIncorrectos = intentosIncorrectos+1
    
    print(f"""\n
                Veamos tus respuestas!
          Intentos correctos: {intentosCorrectos}
          Intentos incorrectos: {intentosIncorrectos}
    """)
    
    if intentosCorrectos == 5:
        nombre = input("¡Felicidades! Has completado el desafío. Por favor, ingresa tu nombre para el Salón de la Fama: ")
        print(f"¡Felicidades, {nombre}! Has sido agregado al Salón de la Fama.")
    else:    
        print(f"Te faltaron/faltó {intentosIncorrectos} aciertos para tener los 5 aciertos\n")
        
 ##Juego Suma nivel 1       
def sumaNivelUno():
    print("Bienvenido al Juego de Suma, este es el primer nivel. Facilito, diviertéte! ")
    intentosCorrectos=0
    intentosIncorrectos=0
    
    for i in range(5):
        num1 = int(randint(1,9))
        num2 = int(randint(1,9))
        respUsuario= int(input(f"¿Cuánto es {num1} + {num2}? "))
        suma = num1+num2
        
        if respUsuario == suma:
            print("Woow Respuesta correcta!!")
            intentosCorrectos = intentosCorrectos+1
        else:
            print("Nono, Respuesta incorrecta")
            intentosIncorrectos = intentosIncorrectos+1
    
    print(f"""\n
                Veamos tus respuestas!
          Intentos correctos: {intentosCorrectos}
          Intentos incorrectos: {intentosIncorrectos}
    """)
    
    if intentosCorrectos == 5:
        print("¡Felicidades! Has alcanzado el nivel 2.")
        sumaNivelDos()
    else:
        print("Para avanzar al nivel 2 debes tener 5 aciertos:D Inténtalo de nuevo.\n")

    return

#########Juego de Restas

def juegoResta():
    print("Bienvenido al Juego de Restas, diviertéte! ")
    print("Debes ingresar el resultado correcto de cada operación para pasar a la siguiente.")
    
    intentosCorrectos=0
    ejercicios=1
    respUsuario=0
    
    while ejercicios <=5:
        num1 = int(randint(10,100))
        num2 = int(randint(1,10))
        resta = num1-num2

        while respUsuario != resta:
            respUsuario = int(input(f"Resta No.{ejercicios}: ¿Cuánto es {num1} - {num2}? "))

            if respUsuario == resta:
                print("¡Respuesta correcta! ¡Sigue con la siguiente operación!\n")
                ejercicios += 1
            else:
                print("Respuesta incorrecta. Inténtalo de nuevo.\n")

    print("¡Felicidades! ¡Completaste todos los ejercicios de resta!")

####Juego de Multiplicaciones
    
def juegoMultiplicaciones():
    print("Bienvenido al Juego de Multiplicación, este es el primer nivel. Facilito, diviertéte! ")
    intentosCorrectos=0
    intentosIncorrectos=0
    ejercicios=0
       
    for i in range (10):
        
        num1 = int(randint(1,10))
        num2 = int(randint(1,10))
        multiplicacion = num1*num2
        ejercicios += 1
        respUsuario= int(input(f"No.{ejercicios}: ¿Cuánto es {num1} x {num2}? "))
        
        if respUsuario == multiplicacion:
            print("Woow Respuesta correcta!!")
            intentosCorrectos=intentosCorrectos+1
        else:
            print(f"Incorrecto, la respuesta correcta era: {multiplicacion}")
            intentosIncorrectos=intentosIncorrectos+1
         
    return intentosCorrectos
    
##Menuuuuuu
    
while True:    
    print("""
.--.--.--.--.--.--.--.--.--.--.--.--.--.
          F u n c i o n e s 
        || M E N Ú DE JUEGOS ||
.--.--.--.--.--.--.--.--.--.--.--.--.--.
         1. Suma
         2. Resta
         3. Multiplicación
         4. SALIR """)
    
    menu = int(input("Elige una opción del menú: "))
    
    if menu==1: #Menú de suma 
        print()
        sumaNivelUno()
            
    ####   
    elif menu==2: #Menú de restas
        print()
        juegoResta()
         
     #####
    elif menu==3:#Menú multiplicación
        print()
        aciertos=juegoMultiplicaciones()
        print(f"""
    \n\n ||Completaste 10 ejercicios con {aciertos} aciertos||
                """)

    elif menu==4:
        print("¡Juega cuando quieras! Saliendo.....")
        break
    else:
        print("Elige una opcion existente (1-4)")


