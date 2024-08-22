valores = [[7, 1, 7, 4],[8, 3, 1, 5],[9, 3, 5, 2],[1, 7, 10, 8]]

suma=0
for renglon in valores:
    for elemento in renglon:
        print(elemento)
        suma=suma+elemento
print(suma)

print()
fil = len(valores)
col = len(valores[0])

print()
print(fil)
print(col)
