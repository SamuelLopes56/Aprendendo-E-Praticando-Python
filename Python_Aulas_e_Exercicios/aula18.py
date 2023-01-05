"""
Índices e fatiamento de strings em Python
"""

"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""

# positivos [012345678] índice 0 = p, índice 1 = y, etc...
texto = "Python s2"
# negativos -[987654321]

print(texto[2])  # Vai aparecer o t pq chamamos essa letra acessando o seu índice
print(texto[6])  # Mesma coisa que o de cima, porém vai aparecer o "espaço" oq chamamos o seu índice

url = "www.google.com.br/"

print(url[:-1])  # Vai imprimir a url do google porém sem a / do final.

nova_string = texto[2:6]  # Fatiamento, o primeiro parâmetro é o índice que começa a stringe e o último é onde acaba ( lembrando que o segundo parâmetro não entra na string. Nesse caso a string começa no "t" (índice 2) e acaba no " "(índice 6), pois eu queria que o fim da string fosse o "n"(índice 5) então eu coloco até o " "(índice 6). Se eu uso o segundo índice como 5 ou seja "n" ele ficaria de fora e a string iria ser "tho" ao invés de "thon".)
print(nova_string)

nova_string2 = texto[:6]  # Aqui como eu não informo o primeiro índice, a string começa do inicio do texto.
print(nova_string2)

nova_string3 = texto[-1]  # Quando se usa números negativos é o mesmo que usar os positivos só que de trás para frente. ( Porém sem o 0 e incrementando o ´´ultimo indice. Ex - se uma string tem de 0 a 8 ( com 0 sendo o primeiro caractere e 8 o último ) de índice, os índices negativos dela são de -9 até -1 ( com -9 sendo o primeiro caractere e -1 o último ). )
print(nova_string3)

nova_string4 = texto[-9:-3]
print(nova_string4)

nova_string5 = texto[0:6:2]  # O tericeiro parâmetro indica quantos caracteres irei pular enquanto monto a string. Nesse caso ele vai montar a stringo do índice 0 até o índice 6 ( lembrando que o 6 não entra na string por ser o último caractere ) pulando de 2 em 2 caracteres. Formando assim a string "Pto".
print(nova_string5)

print(len(texto))

for letra in texto:
    print(letra)
