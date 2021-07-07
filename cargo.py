class cargo:
    secuencia=0
    def __init__(self,cod,des="sin cargo"):
        cargo.secuencia=cargo.secuencia+1
        self.codigo=cod
        self.descripcion=des
if __name__ == "__main__": 
    cargo1=cargo(1,"estudiante")
    print(cargo1.codigo,cargo1.descripcion)
    cargo2=cargo(2,"ingeniero")
    print(cargo2.codigo,cargo2.descripcion)
    cargo3=cargo(3,"admision")
    print(cargo3.codigo,cargo3.descripcion)
    print(cargo.secuencia)
    print(cargo1.secuencia)
    print(cargo2.secuencia)
    print(cargo3.secuencia) 
