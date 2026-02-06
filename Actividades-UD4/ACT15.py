cosa1 = {210, 200, 301, 40, 70, 32}
cosa2 = {101, 7, 140, 30, 200, 40}
comunes = cosa1.intersection(cosa2)
if comunes:
    print("estan en las 2 listas:", comunes)
else:
    print("no hay nada igual en las 2.")