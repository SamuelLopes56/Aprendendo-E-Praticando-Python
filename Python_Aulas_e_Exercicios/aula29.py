"""
Expressão condicional com operador OR
"""



"""
nome = input('Qual o seu nome? ')
if nome:
    print(nome)
else:
    print('Você mão digitou nada.')
"""

# nome = input('Qual o seu nome? ')
# print(nome or 'Você não digitou nada.')
# print(nome or None or False or 0 or 'Você não digitou nada.')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g  # Ele para no primeiro valor True que acha, no caso o 22, se ele testa-se a variável g antes da f ele ia parar no valor 'Luiz'

print(variavel)
