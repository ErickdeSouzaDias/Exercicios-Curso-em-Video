"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""
# Variables
op = ''
# Create the lists
numbers = list()
pairs = list()
odd = list()

# Making the read
while True:
    numbers.append(int(input('Digite um número: ')))  # Add the number at the list.
    while 'S' != op != 'N':  # Response validasion
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if 'S' != op != 'N':
            print('Opção inválida! Tente novamente...')
    if op == 'N':  # End the program.
        break
    op = ''
# Data analysis
for n in numbers:
    if n % 2 == 0:
        pairs.append(n)
    elif n % 2 == 1:
        odd.append(n)
# Display the results.
print(f'Os números digitados foram: {numbers}.')
print(f'Os números impares digitados foram: {odd}.')
print(f'Os números pares digitados foram: {pairs}.')
