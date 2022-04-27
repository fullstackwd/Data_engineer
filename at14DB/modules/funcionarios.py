from modules.postgres import Conector_postgres

banco1 = Conector_postgres(host="127.0.0.1", db="at11DB", user="postgres", password="postgres", port= "5432")

class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    
    def cadastra_funcionario(self):
        '''
        Método que realiza o cadastro dos funcionários no banco de dados
        '''
        try:
            for i in self.nome:
                if i == "'":
                    self.nome = self.nome.replace("'", "''")
            banco1.inserir(f"INSERT INTO funcionario(nome_funcionario) VALUES ('{self.nome}')")
        except Exception as e:
            print(str(e))