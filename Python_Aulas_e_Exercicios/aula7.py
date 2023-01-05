"""
Formatação de strings
"""

nome = 'Luiz'
idade = 32
altura = 1.80
e_maior = idade > 18
data_1 = True
data_atual = 2022
peso = 80

imc = peso / (altura**2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc}')  #isso se chama F-Strings é igual a usar `${}` no javascript
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{2:.2f} {0} {0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))  #esses números nas {} s]ao os índices da função format que correspondem as variáveis. (nome, idade, imc) ou seja (0, 1, 2) o indice começa no 0.
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
