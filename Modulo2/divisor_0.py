"""
División entre 0
Escribe un programa que realice la división de dos números, Si el divisor es 0 envía un
mensaje de error e informa que no se puede realizar la división entre 0. De otra forma,
presenta el resultado de la operación.


"""
print("Este programa realiza la división de 2 números, cuidando que el divisor no sea 0. ")

num = int(input("Dame un primer número: "))
num2 = int(input("Dame un segundo número: "))

if num2 == 0:
    print("El divisor es 0, por lo tanto no puede hacerse la división. Ingrese otro. ")
else:
    div = num/num2
    print(f"El resultado de dividir {num} entre {num2} es {div:.2f}")

