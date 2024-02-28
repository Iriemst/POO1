#1.¿Qué palabra se utiliza en lugar de animal (nombre de la clase) para acceder al atributo patas?

#2 ¿Qué palabra hay que utilizar para crear un nuevo objeto?
class animal:
    #patas = 0 #atributo

    def caminar(self): #metodo
        self.patas = 0  #atributo
        print(f"Caminando con {self.patas} patas")

def main():
    vaca = animal
    vaca.patas= 4
    vaca.caminar()

    pato = animal
    pato.patas= 2
    pato.caminar()

if __name__=="__main__":
    main()