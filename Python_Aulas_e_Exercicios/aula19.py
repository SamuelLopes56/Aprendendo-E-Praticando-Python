"""
While - estrutura de repetição em Python
"""

"""
While em Python
utiliza para realizar ações enquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores
"""

"""
while True:  # Loop infinito
    nome = input("Qual o seu nome? ")
    print(nome)

print("Não será executado.")
"""

"""
x = 0
while x <= 100:
    print(x)
    x = x + 1

print("Acabou!")
"""

"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue  # Quando tiver a palavra "continue" ele não executa o código abaixo da palavra ( contanto que esteja no mesmo escopo que a palavra foi usada, nesse caso no escopo do if )
    
    print(x)
    x = x + 1

print("Acabou!")
"""

"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break  # Parecido com a palabra "continue", porém o break encerra o laço de repetição,

    print(x)
    x = x + 1

print("Acabou!")
"""

"""
x = 0  # Coluna

while x < 10:
    y = 0  # Linha

    while y < 5:
        print(f"X vale {x} e Y vale {y}")
        y += 1

    x += 1  # Isso e a mesmo coisa que x = x + 1 OU o mesmo que x++ do javascript

print("Acabou!")
"""

while True:
    print()
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")
    sair = ""

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Você precisa digitar um número.")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - * /
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print("Operador inválido!")
    
    while sair != 's' and sair != 'n':
        sair = input("Deseja sair? [s]im ou [n]ão: ")
    
    if sair == 's':
        break