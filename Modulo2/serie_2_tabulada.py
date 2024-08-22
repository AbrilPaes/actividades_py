
num = int(input("Dame de qué número quieres la serie numérica: "))

cont=num

while cont<=100:
    print(cont, end= "\t")
    
    if cont%10==0:
        print("\n")
    cont = cont+num

print(f"\nEste ciclo se ejecutó {cont} veces.")

