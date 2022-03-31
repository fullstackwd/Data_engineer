#======================#
#  Tkinter Calculator  #
#----------------------#
#  Konstantinos Thanos #
#   Mathematician, MSc #
#======================#

'''
Verificação e revisão fonte: https://github.com/kostasthanos/Tkinter-Calculator/blob/master/Tkinter_Calculator.py
Visual Soulcode
'''

# importação de pacotes
from tkinter import *
import math
# import numpy as np  # retriar o comentério se não estiver o numpy instalado.
'''
Funções
'''
# Função para adicionar na entrada de exibição de texto
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Função para limpar toda a entrada de exibição de texto
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Função para deletar um por um do último na entrada do display de texto
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

# Função para calcular o fatorial de um número
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    global calc_operator
    result = str(factorial(int(calc_operator)))
    calc_operator = result
    text_input.set(result)

# Função para calcular números trigonométricos de um ângulo
def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    result = str(1/math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

# Função para encontrar a raiz quadrada de um número
def square_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

# Função para encontrar a raiz cubica de um número
def third_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/3)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

# Função para mudar o sinal do número
def sign_change():
    global calc_operator
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp)    

# Function to calculate the percentage of a number
def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)

# Função para encontrar o resultado de uma operação => igual
def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op

'''
Variáveis
'''
sin, cos, tan = math.sin, math.cos, math.tan
log, ln = math.log10, math.log
e = math.exp
p = math.pi
E = '*10**'

tk_calc = Tk()
tk_calc.configure(bg="#f5fffe", bd=10)
tk_calc.title("Calculadora Científica")

calc_operator = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth = 5, bg='#0e59e6', justify='right').grid(columnspan=5, padx = 10, pady = 15)

button_params = {'bd':5, 'fg':'#0e59e6', 'bg':'#f2e516', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#f2e516', 'bg':'#0e59e6', 'font':('sans-serif', 20, 'bold')}

'''
Botões
'''
#--1ª linha--
# Valor absoluto de um número
abs_value = Button(tk_calc, button_params, text='abs',
                   command=lambda:button_click('abs(')).grid(row=1, column=0, sticky="nsew")
# Restante de uma divisão
modulo = Button(tk_calc, button_params, text='mod',
                command=lambda:button_click('%')).grid(row=1, column=1, sticky="nsew")
# Quociente de divisão inteiro
int_div = Button(tk_calc, button_params, text='div',
                 command=lambda:button_click('//')).grid(row=1, column=2, sticky="nsew")
# Fatorial de um número
factorial_button = Button(tk_calc, button_params, text='x!',
                   command=fact_func).grid(row=1, column=3, sticky="nsew")
# número de Euler e
eulers_num = Button(tk_calc, button_params, text='e',
                    command=lambda:button_click(str(math.exp(1)))).grid(row=1, column=4, sticky="nsew")

#---2ª linha--
# Seno de um ângulo em graus
sine = Button(tk_calc, button_params, text='sin',
             command=trig_sin).grid(row=2, column=0, sticky="nsew")
# Cosseno de um ângulo em graus
cosine = Button(tk_calc, button_params, text='cos',
             command=trig_cos).grid(row=2, column=1, sticky="nsew")
# Tangente de um ângulo em graus
tangent = Button(tk_calc, button_params, text='tan',
             command=trig_tan).grid(row=2, column=2, sticky="nsew")
# Cotangente de um ângulo em graus
cotangent = Button(tk_calc, button_params, text='cot',
             command=trig_cot).grid(row=2, column=3, sticky="nsew")
# Número Pi(3,14...) 
pi_num = Button(tk_calc, button_params, text='π',
                command=lambda:button_click(str(math.pi))).grid(row=2, column=4, sticky="nsew")

#--3ª linha--
# Potência de 2
second_power = Button(tk_calc, button_params, text='x\u00B2',
             command=lambda:button_click('**2')).grid(row=3, column=0, sticky="nsew")
# Potência de 3
third_power = Button(tk_calc, button_params, text='x\u00B3',
             command=lambda:button_click('**3')).grid(row=3, column=1, sticky="nsew")
# Potência de n
nth_power = Button(tk_calc, button_params, text='x^n',
             command=lambda:button_click('**')).grid(row=3, column=2, sticky="nsew")
# Número inverso
inv_power = Button(tk_calc, button_params, text='x\u207b\xb9',
             command=lambda:button_click('**(-1)')).grid(row=3, column=3, sticky="nsew")
# Potências de 10
tens_powers = Button(tk_calc, button_params, text='10^x', font=('sans-serif', 15, 'bold'),
                     command=lambda:button_click('10**')).grid(row=3, column=4, sticky="nsew")

#--4ª linha--
# Raiz quadrada de um número
square_root = Button(tk_calc, button_params, text='\u00B2\u221A',
                     command=square_root).grid(row=4, column=0, sticky="nsew")
# Terceira raiz de um número
third_root = Button(tk_calc, button_params, text='\u00B3\u221A',
                    command=third_root).grid(row=4, column=1, sticky="nsew")
# n-ésima raiz de um número
nth_root = Button(tk_calc, button_params, text='\u221A',
                  command=lambda:button_click('**(1/')).grid(row=4, column=2, sticky="nsew")
# Logaritmo de um número com base 10
log_base10 = Button(tk_calc, button_params, text='log\u2081\u2080', font=('sans-serif', 16, 'bold'),
                   command=lambda:button_click('log(')).grid(row=4, column=3, sticky="nsew")
# Logaritmo de um número com base e (ln)
log_basee = Button(tk_calc, button_params, text='ln',
                   command=lambda:button_click('ln(')).grid(row=4, column=4, sticky="nsew")

#--5ª linha--
# Adicionar parêntese esquerdo
left_par = Button(tk_calc, button_params, text='(',
                  command=lambda:button_click('(')).grid(row=5, column=0, sticky="nsew")
# Adicionar parênteses à direita
right_par = Button(tk_calc, button_params, text=')',
                   command=lambda:button_click(')')).grid(row=5, column=1, sticky="nsew")   
# Alterar o sinal de um número
signs = Button(tk_calc, button_params, text='\u00B1',
               command=sign_change).grid(row=5, column=2, sticky="nsew")
# Transformar número em porcentagem
percentage = Button(tk_calc, button_params, text='%',
               command=percent).grid(row=5, column=3, sticky="nsew")
# Calcule a função e^x
ex = Button(tk_calc, button_params, text='e^x',
               command=lambda:button_click('e(')).grid(row=5, column=4, sticky="nsew")

#--6ª linha--
button_7 = Button(tk_calc, button_params_main, text='7',
                  command=lambda:button_click('7')).grid(row=6, column=0, sticky="nsew")
button_8 = Button(tk_calc, button_params_main, text='8',
                  command=lambda:button_click('8')).grid(row=6, column=1, sticky="nsew")
button_9 = Button(tk_calc, button_params_main, text='9',
                  command=lambda:button_click('9')).grid(row=6, column=2, sticky="nsew")
delete_one = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='DEL', command=button_delete, bg='#db1f1f').grid(row=6, column=3, sticky="nsew")
delete_all = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='AC', command=button_clear_all, bg='#bd2008').grid(row=6, column=4, sticky="nsew")

#--7ª linha--
button_4 = Button(tk_calc, button_params_main, text='4',
                  command=lambda:button_click('4')).grid(row=7, column=0, sticky="nsew")
button_5 = Button(tk_calc, button_params_main, text='5',
                  command=lambda:button_click('5')).grid(row=7, column=1, sticky="nsew")
button_6 = Button(tk_calc, button_params_main, text='6',
                  command=lambda:button_click('6')).grid(row=7, column=2, sticky="nsew")
mul = Button(tk_calc, button_params_main, text='*',
             command=lambda:button_click('*')).grid(row=7, column=3, sticky="nsew")
div = Button(tk_calc, button_params_main, text='/',
             command=lambda:button_click('/')).grid(row=7, column=4, sticky="nsew")

#--8ª linha--
button_1 = Button(tk_calc, button_params_main, text='1',
                  command=lambda:button_click('1')).grid(row=8, column=0, sticky="nsew")
button_2 = Button(tk_calc, button_params_main, text='2',
                  command=lambda:button_click('2')).grid(row=8, column=1, sticky="nsew")
button_3 = Button(tk_calc, button_params_main, text='3',
                  command=lambda:button_click('3')).grid(row=8, column=2, sticky="nsew")
add = Button(tk_calc, button_params_main, text='+',
             command=lambda:button_click('+')).grid(row=8, column=3, sticky="nsew")
sub = Button(tk_calc, button_params_main, text='-',
             command=lambda:button_click('-')).grid(row=8, column=4, sticky="nsew")

#--9ª linha--
button_0 = Button(tk_calc, button_params_main, text='0',
                  command=lambda:button_click('0')).grid(row=9, column=0, sticky="nsew")
point = Button(tk_calc, button_params_main, text='.',
               command=lambda:button_click('.')).grid(row=9, column=1, sticky="nsew")
exp = Button(tk_calc, button_params_main, text='EXP', font=('sans-serif', 16, 'bold'),
             command=lambda:button_click(E)).grid(row=9, column=2, sticky="nsew")
equal = Button(tk_calc, button_params_main, text='=',
               command=button_equal).grid(row=9, columnspan=2, column=3, sticky="nsew")


tk_calc.mainloop()