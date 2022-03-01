"""
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que
use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses
abertos e fechados na ordem correta.
"""

expressao = str(input('Digite uma expressão:'))  # Reading the expression.
if expressao.count('(') == 0 and expressao.count(')') == 0:
    print('Essa expressão não possui parenteses, por isso '
          'será resolvida na ordem de operação!')
else:
    if expressao.count('(') == expressao.count(')'):
        print('Expressão válida.')
    else:
        print('Expressão inválida.')
