class Persona:
    def __init__(self, nombre, anios):
        self.nombre= nombre
        self.anios= anios

    def imprimir(self):
        print(self.nombre, "tiene ",self.anios,"años")
    
    def cumpleanios(self):
        self.anios+=+1
        print(self.nombre,"cumple un año", "tiene",self.anios)


def main():
    fabio=Persona("Fabio",18)
    fabio.imprimir()
    fabio.cumpleanios()

    samu=Persona("Samu",54)
    samu.imprimir()
    samu.cumpleanios()
    

if __name__=="__main_persona__":
    main()
        