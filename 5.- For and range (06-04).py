caracter=input("Ingrese un caracter: ")
for indice in range(len(caracter)):
    print(indice,"=",caracter[indice])
cdv=0
for car in caracter:
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A","E","I","O","U"]:
            continue
        else:
            cdv=cdv+1
print("la cantidad de vocales es de: {}".format(cdv))
