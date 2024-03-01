class Crypto:
    def __init__(self, nombre,euros):
        self.nombre= nombre
        self.euros=euros

    def stopLoss(self, min, maxmin):
        self.min= min
        self.max=max
        self.min=0.
        self.max=0.
        
    def imprimir(self):
        print(f"El valor de {self.nombre} es {self.euros} euros")
        print(f"El valor de StopLoss min es:{self.min} y el max: {self.max}")