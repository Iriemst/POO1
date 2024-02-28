
class alumno:
    def __init__(self,nombre,nota):
        self.notas=nota
        self.nombre=nombre

    def imprimir(self):
          self.nombre= ""
          print(self.nombre, "obtiene:",self.nota)

          def promociona(self):
            if self.nota >= 5:
                print("Promociona")
            else:
                print("No promociona")
