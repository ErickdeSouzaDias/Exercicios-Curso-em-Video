
from math import factorial

"""
    Faça um programa que leia um número qualquer e mostre o seu
    fatorial.
"""
manual = 'Método manual'
modulo = 'Usando môdulo'
print(30*'#')
print(f'{manual:^30}')
print(30*'#')
# Método manual
n = -1
while n < 0:
    n = int(input('Digite um número para calcular seu fatorial: '))
    if n < 0:
        print('Valor inválido! Tente novamente.')
m = n
cont = n -1
print(f'Calculando {n}! = {n} x ' if n != 0 and n != 1 else "",end="")
if n == 0:
    print(f'0! é igual a 1.')
elif n == 1:
    print(f'1! = 1 x 1 = 1')
else:
    while cont > 0:
        print(f'{cont}',end=" x " if cont != 1 else "")
        n *= cont
        cont -= 1
    print(f' = {n}')

# Metódo com modulo math

print(30*'#')
print(f'{modulo:^30}')
print(30*'#')
print(f'{m}! = {factorial(m)}')