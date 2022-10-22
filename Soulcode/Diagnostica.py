#!/usr/bin/env python
# coding: utf-8

# ## Avaliação Diagnostica.

# In[ ]:


#1a) Crie um código que apresenta "Parabéns!" caso o usuário insira em sequência os números 1, 2, 3, e 4.

senha = int(input("Digite os números (1234): "))

if senha == 1234:  # Senha 1234 um inteiro (int)
    print('"Parabéns!"')
else:
    print("Sequêcia númerica foi digitada errada.")
    


# In[ ]:


#1b) Crie um código que apresenta "Parabéns!" caso o usuário insira em sequência os números 1, 2, 3, e 4.

senha = input("Digite os números (1234): ")

if senha == "1234":  # Senha "1234" uma string
    print('"Parabéns!"')
else:
    print("Sequêcia númerica foi digitada errada.")
    


# In[ ]:


#2) Crie um código que pede nomes em sequencia, e apresenta a lista completa conforme o usuário digita.

lista = []

def inicio():
    entrada = input("digite uma palavra: ")

    if entrada != "fechar":  # Para fechar o programa deve digitar a palvra: fechar
        lista.append(entrada)
        print(lista)
        inicio()
    else:
        print("execução encerrada.")

inicio()


# In[ ]:


#3) Crie um código em que o usuário digite o código de um estado e o computador apresente o estado por extenso. Ex: RJ > Rio de Janeiro

estados = {}
estados = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}

sigla = input("Digite a sigla do estado: ")

print(estados[sigla])


# In[ ]:


#4a) Crie um código que receba 2 números e resolva a potencia do primeiro ao segundo. Ex: 5², 3³, ...

base = float(input("Digite o número base: "))
expoente = float(input("Digite o número expoente: "))

print("O valor númerico da potência é: "+ str(base**expoente))


# In[ ]:


#4b) Crie um código que receba 2 números e resolva a potencia do primeiro ao segundo. Ex: 5², 3³, ...

import math

base = float(input("Digite o número base: "))
expoente = float(input("Digite o número expoente: "))

print("O valor númerico da potência é: "+ str(math.pow(base, expoente)))


# In[ ]:


#5) Crie um código que conte por quantos segundos uma tecla é pressionada.

import time
  
# Ajuste de variaveis de contagem
contagem_inicio = time.time()  # time.time() => Tempo agora.
contagem_final = contagem_inicio

input("Digite um caracter: ")  # Imprime e lê o caracter escolhido.
            
tempo_aperto = round((time.time() - contagem_final), 2)  # Calcula tempo do acionamento da tecla.
  
print("Tempo de acionamento da tecla: " + str(tempo_aperto) + " ms")  # Imprime na tela o tempo de acionamento da tecla.


# In[ ]:


# 6) Crie um código que receba em sequencia de produtos contendo nome de produto, descrição, preço e quantidade em estoque.

estoque = {'nome':'TNT', 'descricao':'bebida energetica', 'preco':'5.00', 'Qt_estoque':'100'}

print(estoque)


# ## Desafios:

# In[ ]:


#1) Crie um código que receba uma matriz e calcule sua inversa.
# Matriz 3 x 3 - Inversa

import numpy as np 

A = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]]) 

print(np.linalg.inv(A))


# In[ ]:


# Matriz 4 x 4 - Inversa
import numpy as np 

A = np.array([[6,  1, 1,  3], 
              [4, -2, 5,  1], 
              [2,  8, 7,  6], 
              [3,  1, 9,  7]]) 

print(np.linalg.inv(A))


# In[ ]:


# Matriz 2 x 2 dupla - Inversa
import numpy as np 

A = np.array([[[1., 2.], [3., 4.]], 
              [[1 , 3],  [3 , 5]]]) 

print(np.linalg.inv(A))


# In[ ]:


#2) Crie um código que dado o símbolo de um elemento da tabela periódica, este retorne o elemento correspondente e suas informações.

get_ipython().system('pip install periodictable')


# # Desconsiderar item abaixo - Somente testes.

# In[ ]:


"""
 Periodic Table of Elements, by Al Sweigart al@inventwithpython.com
 Displays atomic information for all the elements.
 This code is available at https://nostarch.com/big-book-small-python-programming
 Tags: short, science
"""
  
 # Data from https://en.wikipedia.org/wiki/List_of_chemical_elements
 # Highlight the table, copy it, then paste it into a spreadsheet program
 # like Excel or Google Sheets like in https://invpy.com/elements
 # Then save this file as periodictable.csv.
 # Or download this csv file from https://invpy.com/periodictable.csv
 
import csv, sys, re

# Read in all the data from periodictable.csv.
elementsFile = open('periodictable.csv', encoding='utf-8')
elementsCsvReader = csv.reader(elementsFile)
elements = list(elementsCsvReader)
elementsFile.close()
 
ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
               'Group', 'Period', 'Atomic weight', 'Density',
               'Melting point', 'Boiling point',
               'Specific heat capacity', 'Electronegativity',
               'Abundance in earth\'s crust']
 
# To justify the text, we need to find the longest string in ALL_COLUMNS.
LONGEST_COLUMN = 0
for key in ALL_COLUMNS:
     if len(key) > LONGEST_COLUMN:

        LONGEST_COLUMN = len(key)

# Put all the elements data into a data structure:
ELEMENTS = {}  # The data structure that stores all the element data.
for line in elements:
    element = {'Atomic Number':  line[0],
               'Symbol':         line[1],
               'Element':        line[2],
               'Origin of name': line[3],
               'Group':          line[4],
               'Period':         line[5],
               'Atomic weight':  line[6] + ' u', # atomic mass unit
               'Density':        line[7] + ' g/cm^3', # grams/cubic cm
               'Melting point':  line[8] + ' K', # kelvin
               'Boiling point':  line[9] + ' K', # kelvin
               'Specific heat capacity':      line[10] + ' J/(g*K)',
               'Electronegativity':           line[11],
               'Abundance in earth\'s crust': line[12] + ' mg/kg'}
 
 # Some of the data has bracketed text from Wikipedia that we want to
# remove, such as the atomic weight of Boron:
# "10.81[III][IV][V][VI]" should be "10.81"

for key, value in element.items():
# Remove the [roman numeral] text:
    element[key] = re.sub(r'\[(I|V|X)+\]', '', value)
 
    ELEMENTS[line[0]] = element  # Map the atomic number to the element.
    ELEMENTS[line[1]] = element  # Map the symbol to the element.
 
print('Periodic Table of Elements')
print('By Al Sweigart al@inventwithpython.com')
print()
 
while True:  # Main program loop.
     # Show table and let the user select an element:
    print('''            Periodic Table of Elements
    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og
 
     Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
     Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
    print('Enter a symbol or atomic number to examine, or QUIT to quit.')
    response = input('> ').title()
 
    if response == 'Quit':
         sys.exit()
 
  # Display the selected element's data:
    if response in ELEMENTS:
        for key in ALL_COLUMNS:
            keyJustified = key.rjust(LONGEST_COLUMN)
        print(keyJustified + ': ' + ELEMENTS[response][key])
        input('Press Enter to continue...')
        

