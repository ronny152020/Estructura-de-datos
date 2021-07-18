class descuento:
    def __init__(self):
        pass
    
    def compra (self):
        desc=0.15
        compra=0
        producto=int(input("Ingrese su cuenta: "))
        porce=producto*desc
        total=producto-porce
        print("El total a pagar con descuento es de: ",total)
        
pago=descuento()
pago.compra()
