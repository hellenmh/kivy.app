class Animal : 
    def __init__(self,nome):
        self.nome = nome
          
    def fazer_som (self):
         print("O animal faz algum som.")
        
class Cachorro(Animal):
    def __init__(self, nome,raca):
        super().__init__(nome)
        self.raca = raca 
        
    def fazer_som(self):
        print("O cachorro faz au au!")
    
animal_generico = Animal(input('Digite o nome de um Animal:'))
cachorro1 = Cachorro("Rex","Labrador")
animal_generico.fazer_som()
cachorro1.fazer_som()