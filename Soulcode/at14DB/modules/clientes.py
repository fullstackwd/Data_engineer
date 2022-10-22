from modules.postgres import Conector_postgres

banco1 = Conector_postgres(host="127.0.0.1", db="at11DB", user="postgres", password="postgres", port= "5432")

class Cliente():
    def __init__(self, nome):
        self.nome = nome
        
    #Criando um método para adicionar o cliente no banco de dados:
    def cadastra_cliente(self):
        '''
        Método que realiza o cadastro dos clientes no banco de dados
        '''
        try:
            for i in self.nome:
                if i == "'":
                    self.nome = self.nome.replace("'", "''")
            banco1.inserir(f"INSERT INTO cliente(nome_cliente) VALUES ('{self.nome}')")
        except Exception as e:
            print(str(e))