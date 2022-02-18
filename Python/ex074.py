"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e
o maior valor que estão na tupla.
"""

from random import choices

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sorteados = tuple(choices(numeros, k=5))

print('Os numeros sorteados foram: ', end="")
for numero in sorteados:
    print(f'{numero}',end=" ")
print()

print(f'O maior número sorteado foi {max(sorteados)}.')
print(f'O menor número sorteado foi {min(sorteados)}.')

