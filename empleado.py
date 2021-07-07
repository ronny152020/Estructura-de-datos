from cargo import cargo
class empleado:
    secuencia=0
    def __init__(self,nam,car):
        self.codigo=self.gencodigo()
        self.nombre=nam
        self.cargo=car
        
    def gencodigo(self):
        empleado.secuencia=empleado.secuencia+1
        return empleado.secuencia
    def mostrar(self):
        print("({})- nombre: {} ({}) - cargo: {} ".format(self.codigo,self.nombre,self.codigo,self.cargo.descripcion))
cargo1= cargo("estudiante")
cargo2=cargo("ingeniero")

emp1= empleado("Ronny",cargo1)
emp1.mostrar()
emp2=empleado("Ronny",cargo2)
emp2.mostrar()