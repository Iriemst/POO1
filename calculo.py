class Calculo:
    def __init__(self, numero1,numero2):
        self.numero1= numero1
        self.numero2=numero2

    def suma(self, numero1,numero2):
        resultado= self.numero1 + self.numero2
        print(f"Resultado de la suma de {self.numero1} + {self.numero2} es {resultado}")

    def resta(self, numero1,numero2):
        resultado= self.numero1 - self.numero2
        print(f"Resultado de la resta de {self.numero1} - {self.numero2} es {resultado}")
    
    def multiplicacion(self, numero1,numero2):
        resultado= self.numero1 * self.numero2
        print(f"Resultado de la multiplicacion de {self.numero1} * {self.numero2} es {resultado}")

    def division(self, numero1,numero2):
        resultado= self.numero1 / self.numero2
        print(f"Resultado de la division de {self.numero1} / {self.numero2} es {resultado}")


if __name__=="__main__":
    calculo=Calculo(5,7)
    calculo.suma(5,7)
    calculo.resta(5,7)
    calculo.multiplicacion(5,7)
    calculo.division(5,7)