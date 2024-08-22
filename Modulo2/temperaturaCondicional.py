"""
Actualmente el clima cambia de frio a calor intempestivamente. Un programador ha colocado
un termómetro digital en la puerta de su casa que le indica la temperatura exacta momentos
antes de salir a la calle y con ello podrá vestir de forma adecuada


Según la temperatura :
▫ A 30 o más grados centígrados vestirá “playera sin mangas y short”
▫ Si la temperatura marca menos de 30 pero más de 15 grados vestirá “playera y jeans”
▫ Si el termómetro marca temperatura negativa ( < 0 ) usará su “gabardina y calentadores”
▫ Si la temperatura es cualquier otra, vestirá “sweter y pantalón”

"""
from random import randint

print("¡Este programa determina conocer la temperatura exacta para que salgas! ")
grados = randint(-50,50)
print(f"""La temperatura es de {grados:.2f} grados """)

if grados >= 30:
    print("Playera sin mangas y short")
elif grados>15:
    print("Playera y jeans")
elif grados <0:
    print("Gabardina y calentadores")
else:
    print("Sweter y pantalón")

    
    