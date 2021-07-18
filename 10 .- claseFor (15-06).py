class repetitivo:
    def __init__(self,aprox=8):
        self.num=aprox
        
    def theFor(self):
        nombre="Ronny"
        datos=["Andres",20,True]
        numbers=(20,49,43,10)
        carreras = {"ing": "software", "lic": "educacion", "medico": "cirujano"}
        listaprom =[(80,10),(71,2,31),(10,15,20,1)]
        edadfami=[{"nombre":"ronny","edad":20},{"nombre":"andrea","edad":10},{"nombre":"maritza","edad":43},{"nombre":"angel","edad":49}]
        for r in range(3):
            print("r:{}".format(r))
        for r in range(2,9):
            print("r:{}".format(r))
        for r in range(1,11,3):
            print("r:{}".format(r))
        for r in range(15,4,-2):
            print("r:{}".format(r))  
        for x in range(0,self.num):
            print("x:{}".format(x))
        letras=len(nombre)
        for ubi in range(letras):
            print(nombre[ubi],end= " ")
        
        posdatos=len(datos)
        for ubi in range(posdatos):
            print(datos[ubi],end= " ")
        
        posnum=len(numbers)
        for ubi in range(posnum):
            print(numbers[ubi],end= " ")
            
        for ubi,elem in enumerate(datos):
            print(ubi," ",elem)
        
        for ubicacion in numbers:
            print(ubicacion)
            
        for pos, parte in enumerate(nombre):
            if pos%2==0 and pos!=0:
                print(parte)    
        
        for rama,carrera in carreras.items():
            print(rama,carrera,end=" ")    

repeat= repetitivo()
repeat.theFor()    
