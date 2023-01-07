#Documentação e funções built-in úteis

"""
https://docs.python.org/3/library/stdtypes.html
https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py
https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/17687034#content
"""

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

"""
# isnumeric isdigit isdecimal retorna true ou false depos de verificar todos os caracteres do objeto. Só retorna true se todos passarem no teste.
print(num1.isnumeric())
print(num2.isnumeric())
"""

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print("Não pude converter os números para realizar a soma.")

""" Esse código faz algo parecido que o código de cima, porém ele verifica tudo, se o número é digito, inteiro, float ou negativo.
import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)
 
###########
#  USAGE  #
###########
 
# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True
 
# False
print(is_number('123a'))  # False
"""
