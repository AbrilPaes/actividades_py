def suma(x,y):
    print(x+y)

def suma2(x,y):#Se encarga de la variable de retorno
    return x+y

def suma3(x,y): #Las variables deben separarser por comas
    z=x+y
    return z

#Programa principal
print("Este programa realiza la suma de 2 números.")
num1 = int(input("Dame un número: "))
num2 = int(input("Dame otro número: "))

suma(num1,num2) #La funcion tiene print()

res = suma2(num1,num2)#La función tiene return, por eso se recibe
print(res)

res = suma3(num1,num2)
print(res)
    

    