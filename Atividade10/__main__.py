from modules.postgres import Conector_postgres

if __name__ == "__main__":
    try:
        banco1 = Conector_postgres(host="127.0.0.1", db="acougueDB")
        banco1.inserir('''INSERT INTO ACOUGUE(aves, bovino, ovino, caprino, equino) VALUES
	('Frango Argentino', 'Baby Beef', 'Costeleta Peruana', 'Quarto Baiano', 'Pernil de Jegue');''')
        
        dados = banco1.selecionar('SELECT * FROM ACOUGUE')
        print(dados)
    except Exception as e:
        print(str(e))