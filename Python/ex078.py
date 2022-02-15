"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.
"""

numeros = list()
for cont in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {cont}: ')))
maior = max(numeros)
menor = min(numeros)
print(f'Você digitou os valores {numeros}!')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for p, n in enumerate(numeros):
    if n == maior:
        print(f'{p}..', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for q, m in enumerate(numeros):
    if m == menor:
        print(f'{q}..', end='')
print()
