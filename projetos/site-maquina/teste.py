vlr = 110
notas = {0, 0, 0, 0}

i = 0


while vlr != 0:
    if vlr >= notas[i]:
        resto = vlr % notas[i]
        vlr = resto
        if resto > 0:
            i+=1
    else:
        i+=1


    for notas in range(0, 5):
        print(notas)