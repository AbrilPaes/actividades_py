import os

"""os.rmdir("docs")""" #Eliminar carpetas.. debe estar vacia

if os.path.exists("Resultados.txt"):
    os.remove("Resultados.txt")
else:
    print("El archivo no existe en esta ubicación.")
