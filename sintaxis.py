"""num = 56
num = "79"
if type(num)==int:
    num = num*2
else:
    print("El valor no es numérico")

def mensaje(msg):
    print(msg)

print("Buenos dias")
print("Hola, mi nombre es Ronny")"""

class datosp:
    def __init__(self,dato="definiciones en python"):
        self.frase=dato

    def usovariables(self):
        edad, _peso = 20, 81.5
        nombre = "Ronny Mozo"
        Tipodesexo = "H"
        estudiante = True
        #print("El valor de edad es de {} y es tipo es {}".format (edad,type(edad)))
        usuario =()
        usuario = ("andres_74", "andresmozo316@gmail.com", "7894user","guest78469421114")

        asignaturas = ["EstdDatos", "fisica", "algebra", "poo"]
        asignaturas[0]="Investigacion"
        asignaturas.append("Ingles")

        carreras=()
        carreras = {"ing": "software", "lic": "educacion", "medico": "cirujano"}
        carreras["lic"]="enfermería"
        carreras["M. Sc"]="salud pública"
        print(nombre,nombre[3],nombre[0:6],nombre[-4])
        print(usuario,usuario[1],usuario[1:3],usuario[-4])
        print(asignaturas,asignaturas[1:],asignaturas[::],asignaturas[:2])
        print(carreras,carreras["lic"],carreras["M. Sc"])


    def presentar(self):
        print("Welcome")
        print(self.frase)
ejecutive = datosp()
ejecutive.usovariables()

