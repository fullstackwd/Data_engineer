from modules.postgres import Conector_postgres

if __name__ == "__main__":
    try:
        banco1 = Conector_postgres(host="127.0.0.1", db="loja10DB")
        banco1.create = '''CREATE TABLE relatorio (total_vendas int NOT NULL,maior_venda int NOT NULL
,funcmaxvenda int NOT NULL,fornmax decimal(7,2) NOT NULL,totalcomissao decimal(6,2) NOT NULL);'''
        banco1.inserir('''INSERT INTO relatorio(total_vendas, maior_venda, funcmaxvenda, fornmax, totalcomissao) VALUES
	('8287.91','43.86','50','50','663.02');''')
        
        dados = banco1.selecionar('SELECT * FROM ACOUGUE')
        print(dados)
    except Exception as e:
        print(str(e))