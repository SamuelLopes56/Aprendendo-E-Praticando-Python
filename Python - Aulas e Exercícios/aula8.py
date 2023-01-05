"""
* Criar variáveis para nome (str), idade (int),
* altura (flaot) e pesto (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (basedo na idade e no ano atual)
* Obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)

A saida de tela certa fica assim:
NOME tem IDADE anos, ALTURA de altura e pesa PESOkg.   Com PESO sendo a variável e kg sendo só uma string.
O IMC de NOME é IMC.          O Primeiro IMC é uma string e não a variável
NOME nasceu em ANO_DE_NASCIMENTO.
"""

nome = 'Samuel'
idade = 22
altura = 1.78
peso = 60.0
ano_atual = 2022
imc = peso / (altura**2)
ano_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso:.0f}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}')