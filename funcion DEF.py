def calificacion (notas):
    sum = 0
    for n in notas:
        sum+=n
    return sum/len(notas)
lisnotas=[3,7,10,9,8]
total=calificacion(lisnotas)
print("Sus notas son: {} y su promedio es de: {}".format(lisnotas,total))
if total >= 7:
    print("Usted aprobo el año")
else:
    print("Usted reprobo el año")
