#!/usr/bin/env python
# coding: utf-8

# # Calculadoras.

# In[ ]:


#TODO: completar calculadora, minimo 4 operacoes basicas, raiz e potencia

def somar(x, y):
    return(x + y)

def subtrair(x, y):
    return(x - y)

def multiplicar(x, y):
    return(x * y)

def dividir(x, y):
    try:
        return(x / y)
    except:
        print("Números fora da condição de existncia da divisão.")

def calculadora():
    print("Selecione uma operação")
    print("1-soma 2-subtacao 3-multiplicacao 4-divisao 0-sair")
    selecao = input("opcao: ")
    
    if selecao == "0":
        print("Programa finalizado.")
    
    elif selecao == "1":
        '''
        num1 => 1º valor numerico
        num2 => 2º valor numerico
        '''
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um numero: "))
        print(somar(num1, num2))
        
    elif selecao == "2":
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um numero: "))
        print(subtrair(num1, num2))
        
    elif selecao == "3":
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um numero: "))
        print(multiplicar(num1, num2))
        
    elif selecao == "4":
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um numero: "))
        print(dividir(num1, num2))
        
    else:
        calculadora()
        
calculadora()


# In[ ]:


def inicio():
    print('''Calculadora''')


def calculadora():
    operacao = input('''
Digite a operação matemática que deseja concluir:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    numero_1 = int(input('Por favor, digite o primerio numero: '))
    numero_2 = int(input('Por favor, digite o segundo numero '))

    if operacao == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operacao == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - number_2)

    elif operacao == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operacao == '/':
        print('{} / {} = '.format(number_1, numero_2))
        print(numero_1 / numero_2)

    else:
        print('Você não digitou um operador válido, execute o programa novamente.')

    repetir()


def repetir():
    repetir_calculo = input('''
Deseja calcular novamente?
Digite S para SIM ou N para NÃO.
''')

    if repetir_calculo.upper() == 'S':
        calculadora()
    elif repetir_calculo.upper() == 'N':
        print('Até logo')
    else:
        repetir()


inicio()
calculadora()


# In[ ]:


#TODO: desafio, calculadora cientifica

"""
Favor verifica arquivos: calculadora_simple_cientifica.py e calculadora_cientifica.py
"""


# In[ ]:


#TODO: desafio2, sem usar modulos

"""
Em desenvolvimento.
"""

