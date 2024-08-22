"""
Este programa presenta un esqueleto de menú

"""

print("Este programa presenta un menú ")

while True:
    print("""
.--.--.--.--.--.--.--.--.--.--.--.--.--.
            M E N Ú :
.--.--.--.--.--.--.--.--.--.--.--.--.--.
         1. Mes de verificación
         2. No circula
         3. SALIR """)
    menu = int(input("Elige una opción del menú: "))
    
    if menu==1:
        print("Elegiste mes de verificación")
        placa = int(input("Dime la terminación de tu placa: "))
        if placa==1 or placa==2:
            print("Debes llevar a verificar tu automovil en Enero-Febrero ")
        elif placa==3 or placa==4:
            print("Debes llevar a verificar tu automóvil en Marzo-Abril")
        elif placa==5 or placa==6:
            print("Debes llevar a verificar tu automóvil en Mayo-Junio")
        elif placa==7 or placa==8:
            print("Debes llevar a verificar tu automóvil en Julio-Agosto y Septiembre")
        elif placa==9 or placa==0:
            print("Debes llevar a verificar tu automóvil en Octubre y Noviembre")
        else:
            print("Necesito sólo el último dígito de la terminación de tu placa.")
                      
    elif menu==2:
        print("Elegiste No circula")
        placa = int(input("Dime la terminación de tu placa: "))
        if placa==1 or placa==2:
            print("No circulas los jueves ")
        elif placa==3 or placa==4:
            print("No circulas los miércoles ")
        elif placa==5 or placa==6:
            print("No circulas los viernes ")
        elif placa==7 or placa==8:
            print("No circulas los lunes ")
        elif placa==9 or placa==0:
            print("No circulas los martes ")
        else:
            print("Necesito sólo el último dígito de la terminación de tu placa.")
    elif menu==3:
        print("Hasta pronto")
        break
    else:
        print("Elige una opcion existente")