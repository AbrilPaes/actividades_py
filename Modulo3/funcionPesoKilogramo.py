def transportar(peso):
    if peso<10:
        print("1200")
        return 1200
    elif peso<45:
        print("1200+85 por cada kilo arriba de 10")
        return 1200+85*(peso-10)
    elif peso<=90:
        print("2700+65 por cada kilo arriba de 45")
        return 2700+65*(peso-10)
    else:
        print("3500 + 75 por cada kilo arriba de 90")
        return  3500+75*(peso-10)

#65*5 + 2700