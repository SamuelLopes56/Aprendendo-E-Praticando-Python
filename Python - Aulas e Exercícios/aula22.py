"""
For in - Estrutura de repetição em Python
"""

"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

texto = "Python"

"""
for letra in texto:
    print(letra)
"""

for n in range(10):
    print(n)

print("----------------------------------------")

for n in range(5, 10):
    print(n)

print("----------------------------------------")

for n in range(5, 10, 2):  # Primeiro parâmetro é o inicio, o segundo é o fim e o 3 é o passo ( se vou de 1 em 1, 2 em 2, 3 em 3, etc... )
    print(n)

print("----------------------------------------")

for n in range(5, 10):  # Não vai acontecer nada pq meu inicio é maior que o fim.
    print(n)

print("----------------------------------------")

for n in range(20, 10, -1):  # Ele não incrementa o último caracter. Então se eu quiser que ele mostre o número 10 tenho que fazer ele ir até 9, igual o exemplo abaixo mostra.
    print(n)

print("----------------------------------------")

for n in range(20, 9, -1):
    print(n)

print("----------------------------------------")

for n in range(100):
    if n % 8 == 0:  # Verifica se "n" é múltiplo de 8 ( se o resto da divisão for 0 então é múltiplo de 8 ).
        print(n)

print("#########################################")

texto = "Python"
nova_string = ""
for letra in texto:
    if letra == "t":
        nova_string = nova_string + letra.upper()
    elif letra == "h":
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)
