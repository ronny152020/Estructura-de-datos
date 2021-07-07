class pago_de_horas:
    def __init__(self):
        pass
    
    def horasextras (self):
        horast, pagoh=0,0
        horast=int(input("Ingrese las horas trabajadas: "))
        pagoh=int(input("Ingrese el valor que le pagan por hora: "))
        if horast>40:
            horasex=horast-40
            if horasex>8:
                het=horasex-8
                pagohe=pagoh*2*8+pagoh*3*het
            else:
                pagohe=pagoh*2*horasex
            pagototal=pagoh*40+pagohe
        else:
            pagototal=pagoh*horast
        print("El pago total es de: ",pagototal)
        
    def factorial (self):
        namber=int(input("Ingrese la cantidad de numeros "))
        for i in range(namber):
            numero=int(input("Ingrese un numero "))
            f=1
            for num in range(numero,0,-1):
                f=f*num
            
            print("El factorial del numero {} es de: {}".format(numero,f))
pagoextra=pago_de_horas()
pagoextra.horasextras()
buanidado=pago_de_horas()
buanidado.factorial()