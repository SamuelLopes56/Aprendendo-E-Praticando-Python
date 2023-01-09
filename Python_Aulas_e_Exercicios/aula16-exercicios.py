"""
Todos esses exercícios são da aula "30. Exercícios propostos" do curso de python.
A resolução deles feita pelo professor Luiz Otávio está na aula "Exercícios propostos - Solução" do curso de python.
"""

#PExercício 1:

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

#Resolução do exercício 1:

numero = input("Digite um número inteiro: ")

while not numero.isdigit():
    print("Você precisa diginar um número inteiro!")
    numero = input("Digite um número: ")

numero = int(numero)
if numero % 2 == 0:
    print("O número digitado é par!")
else:
    print("O número digitado é impar!")

#PExercício 2:

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

#Resolução do exercício 2:

horario = input("Informe o horário: ")

while not horario.isdecimal():
    print("Você precisa digitar o horário!")
    horario = input("Informe o horário: ")

horario = float(horario)
if horario >= 12 and horario < 18:
    print("Boa Tarde!")
elif horario >=18 and horario <= 23 :
    print("Boa noite!")
else:
    print("Bom dia!")

#PExercício 3:

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

#Resolução do exercício 3:

nome = input("Informe o seu primeiro nome: ")
letras = len(nome)

if letras <= 4:
    print("Seu nome é curto!")
elif letras >=5 and letras <= 6:
    print("Seu nome é normal!")
else:
    print("Seu nome é muito grande!")
