class buscador:
    def __init__(self,dato):
        self.lista= dato
    
    def recorrerele(self):
        for ele in self.lista:
            print(ele,end=" ")
        
        for ele in self.lista[::-1]:
            print(ele,end=" ")
        
        print()
        for pos,ele in enumerate(self.lista):
            print("[{}]={}  ".format(pos,ele))
        print()
        
        for pos in range(len(self.lista)-1,-1,-1):
            print("[{}]={}  ".format(pos,self.lista[pos]))
        
    def buscar(self,buscado):
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                break
        return pos
               
dato = [5,6,4,9,3,7]
buscado=7
search=buscador(dato)
search.recorrerele()
x=4
R=search.buscar(x)
if R !=1:
    print("el numero {} se encuentra en la posicion [{}] de la lista {} ".format(x,R,search.lista))
else:
    print("el numero {} no se encuentra en la lista {} ".format(x,search.lista))



numerosbuscado=(3,8,7,6,4)
respuesta={}
for valor in numerosbuscado:
    resp=search.buscar(x)
    if resp !=-1: respuesta[x]=resp
print(respuesta)