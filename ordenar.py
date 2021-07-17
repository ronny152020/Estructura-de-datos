class ordenar:
    def __init__(self,cifras):
        self.lista=cifras
        
    def ordennumAsc(self):
        for pos in range(0,len(self.lista)-1):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos]>self.lista[sig]:
                    anexo=self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=anexo
    
    def ordennumDes(self):
        for pos in range(0,len(self.lista)-1):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos]<self.lista[sig]:
                    anexo=self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=anexo
              
    def primero(self):
        return self.lista[0]
    
    def primer1metodo(self):
        primer=self.lista[0]
        self.lista=self.lista[1:]
        return primer
    
    def ultimo(self):
        return self.lista[-1]
    
    def ultimo1metodo(self):
        ultimo=self.lista[-1]
        self.lista=self.lista[:-1]
        return ultimo
                
    def primer2metodo(self):
        primero=self.lista[0]
        anexo=[]
        for first in range(1,len(self.lista)):
            anexo.append(self.lista[first])
        self.lista=anexo
        return primero
    
    def ultimo2metodo(self):
        ultimo=self.lista[-1]
        anexo=[]
        for last in range(0,len(self.lista)-1):
            anexo.append(self.lista[last])
        self.lista=anexo
        return ultimo
    
cifras = [10,5,7,1,3,6]
orden=ordenar(cifras)
orden.ordennumAsc()

print(orden.lista)

orden.ordennumDes()

print(orden.lista)

print(orden.primero())

print(orden.primer1metodo(),orden.lista)

print(orden.ultimo())

print(orden.ultimo1metodo(),orden.lista)

print(orden.primer2metodo(),orden.lista)

print(orden.ultimo2metodo(),orden.lista)