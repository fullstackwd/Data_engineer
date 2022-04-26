import pandas as pd
from modules.postgres import Conector_postgres
from random import randint

if __name__ == "__main__":
    try:
        banco1 = Conector_postgres(host="127.0.0.1", db="at11DB", user="postgres", password="postgres", port= "5432")
        
        banco1.criar("CREATE TABLE IF NOT EXISTS venda("
                     "idvenda serial,"
                     "idproduto integer,"
                     "idvendedor integer,"
                     "valortotal decimal(8,2),"
                     "comissao decimal(8,2),"
                     "CONSTRAINT venda_pk PRIMARY KEY (idvenda),"
                     "CONSTRAINT venda_fk FOREIGN KEY (idproduto) REFERENCES produto (idproduto),"
                     "CONSTRAINT venda_2fk FOREIGN KEY (idvendedor) REFERENCES vendedor (idvendedor)"
                     ");")
        vendas = 20  # Gerador de vendas
        total_vendas = 0
        maior_venda = 0
        idfornecedor_todas_vendas = []
       
        for i in range(vendas):
            venda_idproduto = randint(1,2000)
            venda_idvendedor = randint(1,1000)
            valor_produto = banco1.selecionar(f"SELECT preco FROM produto WHERE idproduto = {venda_idproduto}")
            valor_produto = valor_produto[0]

            valor_total = round(valor_produto * randint(50,5000), 2) 
            valor_total = float(valor_total)
          
            comissao = valor_total*0.08  # Calculo de comissão
            comissao = round(comissao,2)
            
            banco1.inserir(f"INSERT INTO venda(idproduto, idvendedor, valortotal, comissao) VALUES ({venda_idproduto},{venda_idvendedor},{valor_total},{comissao})")

            total_vendas = total_vendas + valor_total

            if valor_total > maior_venda:
                maior_venda = valor_total
                
        print("O valor total vendido foi de R$:",total_vendas)
 
        id_maior_venda = banco1.selecionar(f"SELECT idvendedor FROM venda WHERE valortotal = {maior_venda}")
        id_maior_venda = id_maior_venda[0]
        # id_maior_venda = id_maior_venda[0]
        print("Nome do vendedor com a maior quantidade de vendas: ", banco1.selecionar(f"SELECT nome FROM vendedor WHERE idvendedor = {id_maior_venda}"))
        print("O valor desta venda foi:", maior_venda)
        
        idvendedores_todas_vendas = banco1.selecionar("SELECT idvendedor FROM venda")
        quantidade_vendas = len(idvendedores_todas_vendas)
        idvendedor_mais_vendas = 0
        maior_num_vendas = 0
        idfornecedor_mais_vendas = 0
        maior_numvendas_fornecedor = 0
        for i in range(quantidade_vendas):
       
            num_vendas = idvendedores_todas_vendas.count(idvendedores_todas_vendas[i])
            if num_vendas > maior_num_vendas:
                idvendedor_mais_vendas = idvendedores_todas_vendas[i]
                maior_num_vendas = num_vendas
       
            venda_idproduto = banco1.selecionar(f"SELECT idproduto FROM venda WHERE idvenda = {i+1}")
            venda_idproduto = venda_idproduto[0]
            # venda_idproduto = venda_idproduto[0]
            idfornecedor_todas_vendas.append(banco1.selecionar(f"SELECT idfornecedor FROM produto WHERE idproduto = {venda_idproduto}"))
        
        for i in range(quantidade_vendas):
            num_vendas_fornecedor = idfornecedor_todas_vendas.count(idfornecedor_todas_vendas[i])
            if num_vendas_fornecedor > maior_numvendas_fornecedor:
                maior_numvendas_fornecedor = num_vendas_fornecedor
                idfornecedor_mais_vendas = idfornecedor_todas_vendas[i]
        
        idvendedor_mais_vendas = idvendedor_mais_vendas[0] 
        idfornecedor_mais_vendas = idfornecedor_mais_vendas[0] 
        # idfornecedor_mais_vendas = idfornecedor_mais_vendas[0] 
        print("Nome do vendedor que realizou o maior número de vendas:",banco1.selecionar(f"SELECT nome FROM vendedor WHERE idvendedor = {idvendedor_mais_vendas}"))
        print("A quantidade de vendas que ele efetuou foi:", maior_num_vendas)   
        print("O fornecedor mais utilizado foi:", banco1.selecionar(f"SELECT nome FROM fornecedor WHERE idfornecedor = {idfornecedor_mais_vendas}"))         

        
        banco1.criar(f"CREATE TABLE IF NOT EXISTS comissao("
                     "idcomissao serial,"
                     "idvendedor integer,"
                     "nome varchar(60),"
                     "comissao decimal(8,2),"
                     "CONSTRAINT comissao_pk PRIMARY KEY (idcomissao),"
                     "CONSTRAINT idvendedor_fk FOREIGN KEY (idvendedor) REFERENCES vendedor (idvendedor)"
                     ");")
        
        num_vendedores = len(banco1.selecionar("SELECT idvendedor FROM venda"))
        for i in range(num_vendedores):
            idvendedor = idvendedores_todas_vendas[i]
            idvendedor = idvendedor[0]
            nome = banco1.selecionar(f"SELECT nome FROM vendedor WHERE idvendedor = {idvendedor}")
            nome = nome[0]
            # nome = nome[0]
            for k in nome:
                if k == "'":
                    nome = nome.replace("'", "''")
            comissao = banco1.selecionar(f"SELECT comissao FROM venda WHERE idvendedor = {idvendedor}")
            num_comissoes = len(comissao)
            comissao_vendedor = 0
            for j in range(num_comissoes):
                comissao_lista = comissao[j]
                comissao_lista = comissao_lista[0]
                comissao_vendedor = comissao_vendedor + comissao_lista
            banco1.inserir(f"INSERT INTO comissao (idvendedor, nome, comissao) VALUES ({idvendedor},'{nome}',{comissao_vendedor})")
        tabela_comissoes = banco1.selecionar(f"SELECT idcomissao, nome, comissao FROM comissao")
        df_comissao = pd.DataFrame(tabela_comissoes, columns=["idvendedor","nome","comissao"])
        print(df_comissao)
    except Exception as e:
        print(str(e))