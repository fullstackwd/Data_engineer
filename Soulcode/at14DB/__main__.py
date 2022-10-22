# FAZENDO OS CADASTROS EM MASSA DE TESTE DAS FUNÇÕES:
import csv
from modules.clientes import Cliente
from modules.produtos import Produto
from modules.vendas import Venda
from modules.funcionarios import Funcionario

    # Abrindo o arquivo com os clientes
with open("C:\\at14DB\\clientes.csv", newline='') as csvfile:
    leitor_dados = csv.reader(csvfile, delimiter=',')
            # Inserindo os dados no banco de dados através do método cadastra_cliente
    for row in leitor_dados:
        cliente = Cliente(row[0])
        cliente.cadastra_cliente()

    # Abrindo o arquivo com os produtos:
with open("C:\\at14DB\\produtos.csv", newline ='') as csvfile2:
    leitor_dados = csv.reader(csvfile2, delimiter=',')
            # Inserindo os dados no banco de dados através do método cadastra_produto
    for row in leitor_dados:
        produto = Produto(row[0], row[1])
        produto.cadastra_produto()
                
    # Abrindo o arquivo com os funcionarios:
with open ("C:\\at14DB\\funcionario.csv",newline='') as csvfile3:
    leitor_dados = csv.reader(csvfile3, delimiter= ',')
    for row in leitor_dados:
        funcionario = Funcionario(row[0])
        funcionario.cadastra_funcionario()
        
    # Abrindo o arquivo com as vendas:
with open ("C:\\at14DB\\Vendas.csv", newline='') as csvfile_venda:
    leitor_dados = csv.reader(csvfile_venda, delimiter=',')
    for row in leitor_dados:
        venda = Venda(row[0], row[1], row[2], row[3], row[4])
        venda.cadastra_venda()