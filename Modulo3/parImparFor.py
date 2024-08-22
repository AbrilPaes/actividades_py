"""
Pregunta al usuario cuántos números vas a clasificar
luego, con un for y un contador,
cuenta cuántos pares y cuantos impares recibiste.

"""
numeros=int(input(f"Ingresa los números que quieres clasificar: "))
par=0
impar=0
for i in range (1, numeros+1):
    num = int(input(f"Ingresa numero {i}: "))
    if num%2 == 0:
        par=par+1
    else:
        impar=impar+1

print(f"Los números pares son {par} de los {numeros} que ingresaste. ")
print(f"Los números impares son {impar} de los {numeros} que ingresaste. ")


