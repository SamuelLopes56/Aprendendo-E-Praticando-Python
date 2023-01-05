"""
Variáveis
Iniciar com letra, pode conter números, separar com _ ( underline ), letra minúsculas
"""

nome = 'Luiz'
idade = 32
altura = 1.80
e_maior = idade > 18
data_1 = True
data_atual = 2022
peso = 80
print('Nome:', nome, type(nome))
print('Idade:', idade, type(idade))
print('Altura:', altura, type(altura))
print('É maior de idade?', e_maior, type(e_maior))

print(idade * altura)

imc = peso / (altura**2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
