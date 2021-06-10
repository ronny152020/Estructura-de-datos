#colores_de_la_bandera
color = input("ingrese el segundo color de la bandera del ecuador: ")
while color not in("azul"):
    if color == ".":
        break
    color = input("vuelva a intentar: ")
print("efectivamente ese es el color o usted ingreso un punto: {}".format(color))
