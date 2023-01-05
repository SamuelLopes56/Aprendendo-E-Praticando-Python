"""
Listas em Python
"""

"""
Listas em Python
fatiamento
append (inserir no final), insert(inserir aonde quiser na lista, porém tem que passar o índice aonde quer inserir, e ele vai realocar os índices e valores da lista para encaixar tudo), 
pop(remover o último elemento), del(deletar um elemento ou uma fatia de elementos passando o índice como parâmetro), 
clear(limpar a lista),
extend(juntar duas listas), +(concatenar/juntar duas listas)
min, max
range
"""

"""
#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#        -5   -4   -3   -2   -1
lista[5] = 'Qualquer outra coisa'
print(lista[5])
print(lista[0:4])
"""

"""
l1 = [1,2,3]
l2 = [4,5,6]

# l3 = l1 + l2
l1.extend(l2)  #faz o mesmo que o código comentado acima.
l2.append('b')
l2.insert(0, 'banana')
print(l1)
print(l2)
# print(l3)
"""

"""
l2 = [4,5,6]
print(l2)
l2.insert(0, 'banana')
print(l2)
l2.pop()
print(l2)
"""

"""
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)
l2.insert(0, 'banana')
print(l2)
del(l2[0])
print(l2)
del(l2[3:5])  #Aqui ele ta excluindo uma fatia da lista, do índice 3 até o 5 ( ou seja, removendo os números 4 e 5 )
print(l2)
"""

"""
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l2))  #Pega o maior valor da lista
print(min(l2))  #Pega o menor valor da lista
"""

"""
l1 = list(range(1,10))
# print(l1)
for valor in l1:
    print(valor)
"""

"""
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0
for valor in l2:
    soma = soma + valor

print(soma)
"""

secreto = "perfume"
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você Perdeu!!!')
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Ahhh isso não vale, digite apenas uma letra.")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
       print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
       break
    else:
       print(f'A palavra secreta está assim: {secreto_temporario}.')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
