nombres=['Ana','Abril','Luisa']
coeficiente= .8796
m = [[3, 4, 4],[5, 2, 5],[9, 3, 2],[ 7, 10, 8]]

#abrir el archivo
f = open('Resultados.txt','at', encoding='utf-8')
f.write("\n"+str(m))
f.write("\n"+str(nombres))
f.write("\n"+str(coeficiente))

f.close()