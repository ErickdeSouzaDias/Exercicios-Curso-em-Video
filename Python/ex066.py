"""
Crie um programa que leia números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre
elas (desconsiderando o flag).
"""

cont = soma = n = 0

while True:
    n = int(input('Digite um valor: '))
    if n != 999:
        soma += n
        cont += 1

    if n == 999:
        break
print('Foram diditados {} valores e a soma entre eles é {}.'.format(cont, soma))
