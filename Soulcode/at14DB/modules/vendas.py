from modules.postgres import Conector_postgres
import datetime

banco1 = Conector_postgres(host="127.0.0.1", db="at11DB", user="postgres", password="postgres", port= "5432")
class Venda:
    def __init__(self, data, num_produtos, id_cliente, id_funcionario, id_produto):
        self.data = data
        self.num_produtos = num_produtos
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario
        self.id_produto = id_produto
        
    def cadastra_venda(self):
        '''
        Método que realiza o cadastro das vendas no banco de dados e faz a conferência e atualização do estoque.
        Caso não seja possível efetivar a venda por baixa de estoque, ele imprime os dados da venda em que houve o problema e
        também cadastra em outra tabela, vendas mal sucedidas, para que elas possam ser acompanhadas.
        '''
        try:
            estoque = banco1.selecionar(f"SELECT estoque FROM produto WHERE id_produto = {self.id_produto}")
            estoque = estoque[0]
            estoque = estoque[0]
            self.num_produtos = int(self.num_produtos)
            if self.num_produtos <= estoque:
                banco1.inserir(f"INSERT INTO venda(data_venda, num_produtos, id_cliente, id_funcionario, id_produto) VALUES ('{self.data}',{self.num_produtos},{self.id_cliente},{self.id_funcionario},{self.id_produto})")
                novo_estoque = estoque - self.num_produtos
                banco1.update(f"UPDATE produto SET estoque = {novo_estoque} WHERE id_produto = {self.id_produto}")
            else:
                data_agora = datetime.datetime.now()
                banco1.inserir(f"INSERT INTO log_falha(data_venda, data_registro, num_produtos, id_cliente, id_funcionario, id_produto) VALUES ('{self.data}','{data_agora}', {self.num_produtos}, {self.id_cliente}, {self.id_funcionario},{self.id_produto})")
                print(f"Venda mal sucedida por estoque insuficiente: {self.data}, {self.num_produtos}, {self.id_cliente}, {self.id_funcionario}, {self.id_produto}")
        except Exception as e:
            print(str(e))