"""
Función que genere un string en el cual cambes las letras t por 7,
i por 1, las letras a por * y la e por 3 y se
despliegue dicho string cambiado a pantalla.

"""

print("Este programa genera un texto cifrado. ")
texto=input("Dame un texto para cifrarlo: ")
modifica = texto.replace("t","7")
modifica = texto.replace("i","*")
modifica = texto.replace("a","3")
print()
print(modifica)
