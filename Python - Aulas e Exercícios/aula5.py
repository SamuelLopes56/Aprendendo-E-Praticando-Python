"""
Operadores aritiméticos
+ soma, - subtração, * multiplicação, / divisão, // o resultado da divisão é arredondado para número intiero, 
** exponênciação, % retorna o módulo que é o resto da divisão entre um número e outro,
() alterar a precendência no cálculo
"""

print(10 + 10)
print(10 - 5)
print(10 * 10)
print(10 * 'A')  #Vai repetir 10 vezes a string na tela
print('5' + '5')  #Vai concatenar as duas strings. O operador aritimético + pode realizar soma, porém quando é utilizando entra 2 strings ele junta as duas. Ex.: '2' + '2' = 22 e 2 + '2' = erro ao executar o código.
print(10 / 2)
print(10 // 2)
print(10.5 // 3)
print(10 // 3)
print(2 ** 10)
print(10 % 5)
print(10 % 3)
print(10 / 3)
print(10 // 3)
print(5+2*10)
print((5+2)*10)

"""
Precedência dos Operadores Aritméticos
Assim como aprendemos na matemática, operadores têm uma certa precedência que pode ser alterada usando os parênteses (como descrito na aula anterior).

Abaixo, segue uma lista mais precisa de quais operadores tem maior prioridade na hora de realizar contas mais complexas (de maior para menor precedência).

( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

** - Depois vem a exponenciação

* / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

+  - - Por fim, soma e subtração

Contas com operadores de mesma precedência são realizadas da esquerda para a direita.

Observação: existem muito mais operadores do que estes em Python e todos eles também têm precedência, você pode ver a lista completa em https://docs.python.org/3/reference/expressions.html#operator-precedence (sempre utilize a documentação oficial como reforço caso necessário).

Caso tenha dúvidas, faça testes com números. Por exemplo, olhe para essa conta e tente decifrar como chegar no resultado: 2 + 5 * 3 ** 2 - (23.5 + 23.5) (o resultado é 0.0). Para isso você precisa realizar as contas com maior precedência primeiro.
"""
