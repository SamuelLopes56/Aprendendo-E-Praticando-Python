#len - Quantidade de caracteres

usuario = input("Digite o seu usuário: ")
qtd_caracteres = len(usuario)  #O len() é usado para contar o número de caracteres dentro da variável passada. Espaços também contam.

if qtd_caracteres < 6:
    print("Você precisa digitar pelo menos 6 caracteres")
else:
    print("Você foi cadastrado no sistema")

string1 = input("Digite alguma coisa: ")
string2 = input("Digite outra coisa: ")

print(f"A quantidade total de caracteres digitados foi {len(string1) + len(string2)}")

"""
Observação: De acordo com o professor Luiz Otávio, em python tudo é um objeto. Tanto é que se eu pegar uma variável e
colocar um . no final dela eu vou ver várias funções para utilizar. Exemplo: string1. (posso fazer tanto string1.format() quanto outros)
print(len(string2)) e print(string2._len_()) fazem a mesma coisa, porém o primeiro é a versão simplificada (de escrever) do segundo.
"""