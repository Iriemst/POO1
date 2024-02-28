class persona:
    def __init__(self, nombre, anios):
        self.nombre= nombre
        self.anios= anios

    def imprimir(self):
        print(self.nombre, "tiene ",self.anios,"años")
    
    def cumpleanios(self):
        self.anios=self.anios+1
        print(self.nombre,"cumple un año", "tiene",self.anios)
        