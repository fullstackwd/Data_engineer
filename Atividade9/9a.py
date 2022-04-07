# Crie uma classe em Python para modelar um objeto a sua escolha. 
# Deve conter pelo menos 5 atributos, construtor e getters e setters conforme necessário

class Computador():  
 
    # atributos
    atr1 = "máquina"
    atr2 = "equipamento elétrico"
    atr3 = "processa sinais"
    atr4 = "aquece"
    atr5 = "data Server"
    
        # init metodo ou construtor
    def __init__(self, nome):  
        self.nome = nome 
        
            # A sample method   
    
    def faz(self):  
        print("O Computador é uma", self.atr1) 
        print("O Computador é um ", self.atr2) 
        print("O Computador ", self.atr3) 
        print("O Computador ", self.atr4) 
        print("O Computador pode ser um ", self.atr5) 
        print("O nome do computador é: ", self.nome) 
        
primeiro_comp = Computador('IBM')  # Iniciar o objeto 

print(primeiro_comp.atr1) 
primeiro_comp.faz()
