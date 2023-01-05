"""
Operadores lógicos
and = e lógico
or = ou lógico
not = inversor lógico
in = verifica se algo está incluso de uma expressão / in = em (ptbr) ou contém (ptbr)
not in = inverte o in / not in = não contém (ptbr)
"""

"""
#(Verdadeiro e Verdadeiro) = Verdadeiro
comparacao1 and comparacao2

#(Verdadeiro ou Falso) = Verdadeiro
comparacao1 or comparacao2 = verdadeiro

#(Verdadeiro ou Falso) = Verdadeiro
comparacao1 or comparacao2 = verdadeiro
"""

a = 2
b = 3

if not b > a:  #Aqui ele está invertendo a expressãp, ou seja, ele esta pegando o resultado dessa expressão ( que retorna True ) e mudando o seu valor para False.
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

nome = 'Luiz Otávio.'

if 'u' in nome:
    print("Existe a letra U no seu nome.")
else:
    print("Não existe a letra U no seu nome.")

if 'vio' not in nome:
    print("Não existe o texto no seu nome.")
else:
    print("Existe o texto no seu nome.")

usuario = input("Nome do usuário: ")
senha = input("Senha do usuário: ")

usuario_db = 'luiz'
senha_db = '123456'

if usuario_db == usuario and senha_db == senha:
    print("Você está logado no sistema.")
else:
    print("Usuário ou Senha inválidos")