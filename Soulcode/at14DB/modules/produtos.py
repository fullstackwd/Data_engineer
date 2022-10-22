from modules.postgres import Conector_postgres

banco1 = Conector_postgres(host="127.0.0.1", db="at11DB", user="postgres", password="postgres", port= "5432")

class Produto():
    def __init__(self, nome, estoque):
        self.nome = nome
        self.estoque = estoque 
    
    def cadastra_produto(self):
        '''
        Método que realiza o cadastro dos produtos no banco de dados
        '''
        try:
            for i in self.nome:
                if i == "'":
                    self.nome = self.nome.replace("'", "''")
            banco1.inserir(f"INSERT INTO produto(nome_produto, estoque) VALUES ('{self.nome}','{self.estoque}')")
        except Exception as e:
            print(str(e))