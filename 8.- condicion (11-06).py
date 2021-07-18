class condicion:
    def __init__(self,n1,n2):
        self.numero1=n1
        self.numero2=n2
        numero = self.numero1+self.numero2
        self.numero3=numero
    def condicion(self):
        if self.numero1 == self.numero2:
            print("numero1: {} y numero2: {} son iguales".format(self.numero1,self.numero2))
        elif self.numero1 < self.numero3:
            print("numero1 {} es menor que numero3 {}".format(self.numero1,self.numero3))
        else:
            print("no son iguales")
        print("fin")
        
condi1 = condicion(14,9)
print(condi1.numero3)
print(condi1.condicion())