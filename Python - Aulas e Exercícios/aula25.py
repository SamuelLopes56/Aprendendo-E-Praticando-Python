"""
Split, Join e Enumerate em Python
"""

"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteráveis
"""

string = "O Brasil é o país do futebol, o Brasil é penta."
lista1 = string.split(' ')  # Aqui ele corta a string sempre que tem um ' ' ( espaço )
lista2 = string.split(',')  # Aqui ele corta a string sempre que tem uma ',' ( vírgula )
# print(lista1)
# print(lista2)

"""
for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase.')
"""

"""
palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x).')
"""

"""
for valor in lista2:
    print(valor.strip().capitalize())  # A função strip remove espaços do início e do fim da string. - - # E o capitalize deixou o primeiro '0' maiúsculo.
"""

"""
string2 = 'O Brasil é penta.'
lista3 = string2.split(' ')
string3 = ','.join(lista3)  #O primeiro argumento ( nesse caoso é a ',' ) é o elemento de escolha para separar os elementos da lista que irei montar com o join.

print(string2)
print(lista3)
print(string3)
"""

"""
string2 = 'O Brasil é penta.'
lista3 = string2.split(' ')

for indice, valor in enumerate(lista3):
    print(indice, valor, lista3[indice])
"""

lista4 = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria'],
]

lista5 = ['Luiz', 'João', 'Maria']

for indice, nome in lista4:
    print(indice, nome)

print()

for indice, nome in enumerate(lista5):
    print(indice, nome)
