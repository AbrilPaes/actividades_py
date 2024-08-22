def incremento(n):
    n=n+1
    print(f"\t Dentro de la función es {n} ")
    return n

#Pp
x=1
print(f"Antes de la llamada, x es {x} ")
x=incremento(x)
print(f"Después de la llamada, x es {x}")