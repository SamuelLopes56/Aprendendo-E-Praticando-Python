"""
Iterando strings com while em Python
"""
#        índices
#        0123456789......................33 (O último índice é o 33 mas a frase tem 34 índices, ou seja, 34 elementos. O zero também conta)

"""
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0

while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1
"""

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ""

"""
while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1
"""

"""
while contador < tamanho_frase:
    # print(frase[contador], contador)
    nova_string += frase[contador]
    # print(nova_string)
    contador += 1
print(nova_string)
"""

"""
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    # print(frase[contador], contador)
    # nova_string += frase[contador]
    # print(nova_string)
    contador += 1
print(nova_string)
"""

input_do_usuario = input("Qual letra deseja colocar maiúscula: ")
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    # print(frase[contador], contador)
    # nova_string += frase[contador]
    # print(nova_string)
    contador += 1
print(nova_string)
