
# BC17 - Projeto Final

# objetivo: usa a API do site coinmarketcap.com para resgatar as datas de criação das criptomoedas, gerando um arquivo json
# autor: carlos bahia

import requests
import secrets
import pandas as pd
import json
import datetime
from datetime import date, timedelta

# urls para consulta com a API
#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
#url = 'https://coinmarketcap.com/api/documentation/v1/#operation/v1/exchange'
#url = 'https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeInfo'
#/v1/exchange/info

parameters = {
  'start':'1',
  'limit':'5000'

}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '3d301cc4-11d4-4501-8490-eb1e836a7222',
}

r = requests.get(url,headers = headers, params=parameters)
print('')
print('resposta da consulta ', r)
print('')

from pprint import pprint as pp
#pp(r.json())
temp = r.json()

df = pd.DataFrame(json) # poderia trabalhar com json, mas preferi Cria um dataframe
total_series = df.columns.tolist() # Lista de colunas



pp(r.json()['data'][0])

#first_historical_data

