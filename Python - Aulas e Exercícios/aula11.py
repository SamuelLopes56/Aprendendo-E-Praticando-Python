"""
Operadores relacionais
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
"""

idade = int(input("Informe a sua idade: "))
if idade >= 18 and idade <= 30:
    print("Empréstimo liberado")
else:
    print("Empréstimo negado")
