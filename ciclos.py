class periodo:
    def __init__ (self,num=45):
        self.numero=num
    letra=""
    def thewhile(self):
        print("dentro de la clase",self.numero)
        letra=""
        while letra not in("a","e","i","o","u"):
            letra = input("Ingrese una vocal: ")
            letra = letra.lower()
            
        print("Efectivamente la letra {} es una vocal".format(letra))
        
periodo1 = periodo()
print("fuera de la clase",periodo1.numero)
print(periodo1.thewhile)
periodo1.thewhile()
