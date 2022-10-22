class Cachorro:  

    # Variavel de classe
    animal = 'cao'      

    # init metodo de construcao  
    def __init__(self, late):  

        # Variavel de objeto (instancia) 
        self.late = late              

    # adiciona variavel de objeto
    def setRaca(self, Raca):  
        self.Raca = Raca  

    # adiciona outra variaval de objeto      
    def getRaca(self):      
        return self.Raca     

# codigo executor  
nome = Cachorro("Huss")  
nome.setRaca("Pastor Alemão")  
print(nome.getRaca())
