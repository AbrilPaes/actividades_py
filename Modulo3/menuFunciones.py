def segundos(s):
    dias=s//86400
    ss=s%86400
    horas=ss//3600
    ss=ss%3600
    minu=ss//60
    ss=ss%ss%60
    print(f"{s} segundos equivale a: \n{dias} días, \n {horas} horas, \n{minu} minutos, \n{ss} segundos. ")
    
def pies_cm(p):
    return (p*30.48)

def volumen(r):
    volumen = (4* 3.14 * r ** 3)/3
    return volumen


while True:    
    print("""
.--.--.--.--.--.--.--.--.--.--.--.--.--.
          F u n c i o n e s 
               M E N Ú  
.--.--.--.--.--.--.--.--.--.--.--.--.--.
         1. Segundos a días, horas, minutos
         2. Pies a centímetros
         3. Volumen Esfera
         4. SALIR """)
    
    menu = int(input("Elige una opción del menú: "))
    
    if menu==1: #Menú de días 
        segCantidad= int(input("Ingresa los segundos que quieres convertir: "))                    
        segundos(segCantidad)   
            
    ####   
    elif menu==2: #Menú de conversión de pies a cm
        piesCantidad= float(input("Ingresa los pies que quieres convertir: "))
        convertir= pies_cm(piesCantidad)
        print(f"{piesCantidad} pies, es igual a {convertir:.2f} cm")
         
     #####
    elif menu==3:#Calcular volumen
        radio= int(input("Ingresa el radio de la esfera en metros: "))
        esferaR= volumen(radio)
        print((f"El volumen de la es esfera es {esferaR:.2f} metros cúbicos"))
        
    elif menu==4:
        print("Saliendo")
        break
    else:
        print("Elige una opcion existente (1-4)")


