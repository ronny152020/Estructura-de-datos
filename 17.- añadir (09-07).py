class añadir:
    def __init__(self,cifras):
        self.terminos=cifras
        
    def ordennumAsc(self):
        for pos in range(0,len(self.terminos)-1):
            for sig in range(pos+1,len(self.terminos)):
                if self.terminos[pos]>self.terminos[sig]:
                    anexo=self.terminos[pos]
                    self.terminos[pos]=self.terminos[sig]
                    self.terminos[sig]=anexo
    
    def añadirnum(self,numero):
        self.ordennumAsc()
        anexo=[]
        for pos,ele in enumerate(self.terminos):
            if numero<ele:
                anexo.append(numero)
                break
        self.terminos=cifras
        self.terminos=self.terminos[0:pos]+anexo+self.terminos[pos:]
        
    def añadirnum2(self,numero):
        self.ordennumAsc()
        anexo=[]
        for pos,ele in enumerate(self.terminos):
            if numero<ele:
                break
        self.terminos=cifras
        for i in range(pos):
            anexo.append(self.terminos[i])
        anexo.append(numero)
        for k in range(pos,len(self.terminos)):
            anexo.append(self.terminos[k])
        self.terminos=anexo
        
    def añadir2metodo(self,num):
        self.terminos=cifras
        self.terminos.append(num)
        self.ordennumAsc()
        
    def eliminar(self,num):
        conf=False
        for pos,ele in enumerate(self.terminos):
            if num==ele:
                conf=True
                break
        if conf:
            self.terminos=cifras
            self.terminos=self.terminos[0:pos]+self.terminos[pos+1:]
        return conf
       
cifras=[7,3,8,10,21,9]
agregar=añadir(cifras)
print(agregar.añadirnum(11))
print(agregar.terminos)
print(agregar.añadirnum2(6))
print(agregar.terminos)
print(agregar.añadir2metodo(15))
print(agregar.terminos)

if agregar.eliminar(10)==True:
    print("El numero si se encontro en la lista y a sido eliminado",agregar.terminos)
else:
    print("El numero no se encontro en la lista, asi que queda intacta",agregar.terminos)
