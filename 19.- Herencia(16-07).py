class logica:
    def __init__(self,dato):
        self.lista=dato
        self.estado=True
    
    def par(self,numero):
        res=numero%2
        if res == 0:
            print("{} es Par".format(numero))
        else:
            print("{} es Impar".format(numero))
    
    def par2metodo(self,numero):
        res = numero%2
        return res
    
    def divisores(self,termino):
        divisores=[]
        for divisor in range(1,termino):
            res = termino%divisor
            if res == 0:
                divisores.append(divisor)
        return divisores
    
    def perfecto(self,namber):
        acu=0
        for divisor in range(1,namber):
            res = namber%divisor
            if res==0:
                acu=acu+divisor
        return acu
    
    def sumapares(self):
        acu=0
        for num in self.lista:
            if self.par2metodo(num)==0:
                acu=acu+num
        return acu

# fundamento=logica([2,7,4,6,9])
# print(fundamento.sumapares())

class ejercicios(logica):
    def __init__(self,numeros,valor):
        super().__init__(numeros)
    
    def suma(self,n1,n2):
        if super().par2metodo(n1)==0:
            return (n1+n2)*2
        else:
            return (n1+n2)
    
    def resta(self,n1,n2):
        return n1-n2
    
    def pares(self,numero):
        res = numero%2
        if res == 0:
            print(numero,"Es par")
        else:
            print(numero,"Es impar")
            
termino = ejercicios([3,6,8],20)
print(termino.pares(12))
print(termino.suma(5,6))
            
    
    
