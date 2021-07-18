#numero_entero
numero = int(input("Ingrese un numero: "))
if numero > 0:
    print("El numero entero es positivo")
elif numero == 0:
    print("El numero es cero")
else:
    print("El numero es negativo")
print("ok")if type(numero) == int else print("")
