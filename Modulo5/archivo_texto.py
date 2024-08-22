f=open('Capitulo1.txt','rt', encoding='utf-8')

#texto =f.read(25) #Se agrega valor numérico para leer los primeros # del archivo
#print(texto)

#recorre el archivo por párrafos
for renglon in f:
    #print(renglon)
    if " en " in renglon:
        renglon = renglon.replace(' en ', ' EN ')
    print(renglon)
    
f.close()#para cada open debe haber un close
