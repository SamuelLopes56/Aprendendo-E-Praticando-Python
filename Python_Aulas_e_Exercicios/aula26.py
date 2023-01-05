"""
Desempacotamento de listas em Python
"""

"""
Desempacotamento de listas em Python
"""

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 100]
lista2 = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 100]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista
n43, n44, *_ = lista2  # O *_ indica que eu não vou usar o resto da lista no código.

print(n2)
print(outra_lista)
print(ultimo_da_lista)
