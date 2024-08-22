#Autor: Abril Pacheco Espinosa

"""
Este programa presenta la resolución del Reto Módulo 2
"Hotel Hard Rock Nuevo Vallarta"

"""
from random import randint #randint es una funcion que genera numeros random enteros

print(f"""Este programa presenta un menú del Hotel Hard Rock Nuevo Vallarta siempre y cuando
tu estancia en él, sea mayor a 3 noches\n""")

numNoches = int(input("¿Cuántas noches se hospedará?: "))

if numNoches >3:
    saldo = 2000

    print(f"""\n|¡ADVERTENCIA!|Las amenidades solicitadas no pueden ser intercambiadas por otras
y su cancelación no implica la devolución de su bono.""")
    while True:
    
        print("""
    .--.--.--.--.--.--.--.--.--.--.--.--.--.
           Hotel Hard Rock Nuevo Vallarta
                   M E N Ú  
    .--.--.--.--.--.--.--.--.--.--.--.--.--.
             1. Paseos
             2. Spa
             3. Juego en línea
             4. SALIR """)
        
        menu = int(input("Elige una opción del menú: "))
        
        if menu==1: #Submenú de paseos 
                                
            print("""\t\t\t  S u b m e n ú -Paseos-
                        1. Paseo en globo $800
                        2. Paseo en bicicleta $500""")
            
            opcion = int(input("Elige una opcion: "))
            
            if opcion==1: #Paseo en globo
                if saldo>= 800:
                    saldo=saldo-800            
                else:
                    print(f"**** Saldo insuficiente.. Tienes ${saldo:.2f}****")
            elif opcion==2:#Paseo en bicicleta
                if saldo>=500:
                    saldo=saldo-500
                else:
                    print(f"**** Saldo insuficiente.. Tienes ${saldo:.2f}****")
            else:
                print("Opción no válida.")
                
            print(f"Saldo actual de ${saldo:.2f}")     
                
        ####   
        elif menu==2: #Submenú de Spa
             print("""\n\t\t\t  S u b m e n ú -Spa-
                        1. Masaje relajante completo $600
                        2. Exfoliación $250""")
             
             opcion = int(input("Elige una opcion: "))
             
             if opcion ==1:
                 if saldo>=600:
                    saldo=saldo-600
                 else:
                    print(f"**** Saldo insuficiente..Tienes ${saldo:.2f}****")
             elif opcion==2:
                if saldo>=250:
                        saldo=saldo-250
                else:
                    print(f"**** Saldo insuficiente..Tienes ${saldo:.2f}****")
             else:
                print("**** Opción incorrecta....")
                
             print(f"Saldo actual de ${saldo:.2f}") 
         #####
        elif menu==3:#Juego
            print("3")
            numSecreto = int(randint(1,100))
            numUsuario = 0
            intentos = 1
            maximosIntentos = 8
            while numUsuario!=numSecreto:
                numUsuario = int(input(f" Me indicas un número entre 1 y 100, intento {intentos}: " ))
                if numUsuario == numSecreto:
                    print(f"""\n
                     ================================================================================
                       \t Acertaste el número era {numUsuario}, lo hiciste en {intentos} intento/s 
                       \t GANASTE UNA ENTRADA GRATIS A LA NOCHE DE CASINO DEL HOTEL              
                     ===============================================================================
                        """)
                elif numUsuario>numSecreto:
                    print("El número secreto es menor.")
                else:
                    print("El número secreo es mayor")
                intentos = intentos+1
                if intentos > maximosIntentos:
                    print(f"Se acabaron tus 8 intentos, el número era =|{numSecreto}|=")
                    break
            
        elif menu==4:
            if saldo == 2000:
                print(f"""\nTienda de Regalos tiene un pin Hard Rock para que lo lleves
                como recuerdo de su estancia.""")
                print(f"Tu saldo final es de ${saldo}, ¡Hasta pronto!")
            else:
                print(f"Tu saldo final es de ${saldo}")
                print("¡Hasta pronto!")
            break
        
        else:
            print("Elige una opcion existente (1-4)")
else:
    print("¡Bienvenido!.")