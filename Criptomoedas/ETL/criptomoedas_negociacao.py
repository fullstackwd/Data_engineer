
# BC17 - Projeto Final

# objetivo: transforma um arquivo json em df
# autor: carlos bahia

import pandas as pd
pd.set_option('display.max_columns',25)

# ler arquivo .json com pandas
json = pd.read_json('criptomoedas_negociacao.json')
# print(json)
df = pd.DataFrame(json) # poderia trabalhar com json, mas preferi Cria um dataframe
#imprimir com todas as colunas do dataframe
# print(df.)
print(df[1:30].to_string())
total_series = df.columns.tolist() # Lista de colunas
print(total_series)
# print(arquivo)

# selecionando o ano e mes
df['ano_mes'] = df.first_historical_data.str.slice(0, 7)
df['ano'] = df.first_historical_data.str.slice(0, 4)

cripto_mes = df['ano_mes'].copy()  # para pegar ano e mês
cripto_mes = df['ano'].copy()  # para pegar ano e mês

# gravando em Excel para usar no Data Studio
cripto_mes.to_excel("cripto_ano_mes.xlsx")






