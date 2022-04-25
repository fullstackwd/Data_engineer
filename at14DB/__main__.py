# Importação de módulos, bibliotecas e funções necessários:
import csv
import pandas as pd
import numpy as np
import statistics as st
from modules.postgres import Conector_postgres
from datetime import datetime

banco1 = Conector_postgres(host="127.0.0.1", db="at11DB", user="postgres", password="postgres", port= "5432") # Insira aqui os seus dados!

# Função que vai armazenar o log:
def log(msg):
    data = datetime.now()
    user = banco1.get_user()
    banco1.inserir(f"INSERT INTO log_tabelas(usuario, dt_log, msg_log) VALUES ('{user}','{data}','{msg}')")

# Função que vai fazer os blocos
def criador_blocos(num1, num2):
    bloco = banco1.selecionar(f"SELECT * FROM dados WHERE id_dados BETWEEN {num1} AND {num2} ORDER BY data_dados")
    return bloco

if __name__ == '__main__':
    try:
        log("Carregamento de dados iniciado")
    # Importando os arquivos do CSV:
        #Para o arquivo DADOS1.csv:
        log("Lendo dados1")
        with open('C:\\at14DB\\MOCK_DATA1000.csv', newline='') as csvfile:
            leitor_dados = csv.reader(csvfile, delimiter=',')
            dados1 = []
            # log("Tratando os dados1 - removendo valores faltantes")
            for row in leitor_dados:
                # Tratando os dados, para não incluir linhas com valores nulos na tabela:
                if row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '' and row[5] != '' and row[6] != ':
                    dados1.append(row)  
            dados1.pop(0) # Removendo os títulos das colunas
        #Para o arquivo DADOS2.csv
        log("Lendo dados2")
        with open('C:\\at14DB\\MOCK_DATA1000.csv', newline='') as csvfile2:
            leitor_dados2 = csv.reader(csvfile2, delimiter= ',')
            dados2 = []
            # log("Tratando os dados2 - removendo valores faltantes")
            for row in leitor_dados2:
                # Tratando os dados, para removeer os valores nulos:
                if row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '' and row[5] != '' and row[6] != ':
                    dados2.append(row)
            dados2.pop(0) #Removendo os títulos das colunas
    # Passando os nossos dados para as tabelas do postgres:
            #Para evitar que os dados sejam passados mais de uma vez para as tabelas:
        if len(banco1.selecionar('SELECT * FROM dados')) < 1: #Evitando que os dados sejam inseridos mais de uma vez
            log("Adicionando os valores na tabela dados")
            for i in range(len(dados1)):
                log(f"Inserindo a {i+1}ª linha de valores de dados1 na tabela dados")
                banco1.inserir(f"INSERT INTO dados(data_dados, valor_dados) VALUES ('{dados1[i][1]}','{dados1[i][2]}')") 
            for i in range(len(dados2)):       
                log(f"Inserindo a {i+1}ª linha de valores de dados2 na tabela dados")
                banco1.inserir(f"INSERT INTO dados(data_dados, valor_dados) VALUES ('{dados2[i][1]}','{dados2[i][2]}')") 
    # Fazendo a leitura do banco em blocos de 50 registros - total de 38 blocos:
        num1 = 0
        num2 = 0
        num_blocos = 0
        blocos = [] # A LISTA QUE VAI RECEBER TODOS OS BLOCOS DE DADDOS
        for i in range(len(banco1.selecionar("SELECT * FROM dados"))):
            if i % 50 == 0:
                num1 = i + 1
                num2 = i + 50
                blocos.append(criador_blocos(num1,num2))
                num_blocos += 1                
    # Inserindo os dados na tabela com as informações de cada bloco e preparando um data frame para melhor visualizção no Python: 
        tabela_relacoes = []
        row = []
        for i in range(num_blocos):
            row = contas(blocos[i])
            tabela_relacoes.append(row)
            #Para evitar que os dados sejam inseridos na tabela mais de uma vez:
            if len(banco1.selecionar("SELECT * FROM dados_blocos")) < 1:
                log(f"Inserindo as estatísticas do bloco de dados {i+1} na tabela dados_blocos")
                banco1.inserir(f"INSERT INTO dados_blocos(media, mediana, moda, desvio_padrao, maximo, minimo, inicio, fim) VALUES ({row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},'{row[6]}','{row[7]}')" )
        df_relacoes = pd.DataFrame(tabela_relacoes, columns=['Média', 'Mediana', 'Moda', 'Desvio Padrão', 'Máximo', 'Mínimo', 'Início', 'Fim'])
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("------------------------TABELA COM AS ESTATÍSTICAS DOS BLOCOS DE 50 DADOS DOS ARQUIVOS SELECIONADOS-------------------------\n")
        print(df_relacoes)
        print("----------------------------------------------------------------------------------------------------------------------------")

    # Possibilitando que o usuário acesse facilmente os dados de um dos blocos:
        while True:
            try:
                opcao1 = input("Deseja Verificar os valores de algum dos blocos da tabela dados? [S/N]: ")
                if opcao1 == 'N' or opcao1 == 'n':
                    break
                elif opcao1 == 'S' or opcao1 == 's':
                    opcao2 = int(input(f"Os dados foram divididos em {num_blocos} blocos. Digite o número do bloco que deseja visualizar (entre 1 e 38): "))
                    df_bloco = pd.DataFrame(blocos[opcao2-1], columns = ['id', 'Data', 'Valor'])
                    print("---------------------------------")
                    print(f"--------DADOS DO BLOCO {opcao2}--------\n")
                    print(df_bloco)
                    print("---------------------------------")
                else:
                    print("Opção inválida!")
            except Exception as e:
                print('Ocorreu um erro! Tente novamente e siga as instruções :)')
        print("----------------------------------------------------------------------------------------------------------------------------")
        
    # Possibilitando que o usuário realize o acesso do registro log do banco de dados:
        tabela_log = []
        opcao3 = input("Deseja acessar o histórico de registros e log? [S/N]")
        if opcao3 == 'S' or opcao3 == 's':
            print("---------------------------------------------------------------------------------------------------\n")
            tabela_log = banco1.selecionar('SELECT * FROM log_tabelas')
            df_log = pd.DataFrame(tabela_log, columns = ["id_log", "usuario", "dt_log", "log_msg"])
            print(df_log)
            print("---------------------------------------------------------------------------------------------------")
            print("Programa encerrado.")
            
        elif opcao3 != 'N' or opcao3 != 'n':
            print("Programa encerrado.")
    except Exception as e:
        print(str(e))