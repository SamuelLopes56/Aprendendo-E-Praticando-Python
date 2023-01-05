"""
Formatando valores em Python
"""

"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float) - Ex :.2f
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(f"{divisao:.2f}")

num_3 = 1
print(f"{num_3:0>10}")

num_4 = 1150
print(f"{num_4:0^10}")

print(f"{num_4:.2f}")

print(f"{num_4:0>10.2f}")

nome = "Luiz Otávio"
print(f"{nome:#^50}")  #Lembrando que esses 50 # que vão ser adicionados na verdade são, 50 - 11 (quantidade de caracteres na variável nome) e metade desse resultado var para cada lado. Já que o nome foi definido para ficar no meio e os # irem completando nos lados.
nome_formatado = "{:@>15}".format(nome)
print(nome_formatado)

"""
nome = nome.ljust(20, '#')  #Método feito para preencher o resto das caracteres informados no primeiro parâmetro ( 20 ) com o que for informado no segundo parâmetro ( "#" ).
print(nome)
"""
nome2 = "ROMÁRIO ronaldinho oIeE"
print(nome2.lower())  # Tudo minúsculo
print(nome2.upper())  # Tudo maiúsculo
print(nome2.title())  # Primeiras letras maiúsculas e o resto da palavra minúsculo
