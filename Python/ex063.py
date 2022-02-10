"""

     Escreva um programa que leia um número N inteiro qualquer e mostre na tela
     os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

     0 – 1 – 1 – 2 – 3 – 5 – 8

"""

print(f'{30*"#"}')
print(f'{"Sequência de Fibonacci":^30}')
print(f'{30*"#"}')

repet = int(input('Quantos termos desja mostrar? '))

cont = 0
ant = 0
suc = 1
termo = 1
print(f'{100*"~":<}')
while cont <= repet:
    print(f'{termo}, ',end="")
    termo = ant+suc
    ant = suc
    suc = termo
    cont += 1
print('FIM')
print(f'{100 * "~":<}')
