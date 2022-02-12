"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

valores = (n1, n2, n3, n4)

print(f'O numero 9 foi digitado {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O número 3 foi encontrado na {valores.index(3)}.')

for num in valores:
    if valores.index(num) == 0 and num % 2 == 0:
        print('Os números PARES digitados foram: ', end="")
    if num % 2 == 0:
        print(f'{num}', end=" ")
print()
