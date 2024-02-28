class alumno:
    def imprimir(self):
          self.nota= 0
          self.nombre= ""
          print(self.nombre, "obtiene:",self.nota)

          def promociona(self):
            self.nota= 0
            self.nombre= ""
            if self.nota >= 5:
                print("Promociona")
            else:
                print("No promociona")

def main():
    jorge=alumno()
    jorge.nota= 7
    jorge.imprimir

    maria=alumno()
    maria.nota= 3
    maria.imprimir

if __name__=="__main__":
    main()