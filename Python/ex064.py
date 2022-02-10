"""
    Crie um programa que leia vários números inteiros pelo teclado.
    O programa só vai parar quando o usuário digitar o valor 999,
    que é a condição de parada. No final, mostre quantos números
    foram digitados e qual foi a soma entre eles (desconsiderando o flag)
"""

flag = 0
soma, cont = 0,0
while flag != 999:
    n = int(input('Digite qualquer valor[999] - Sair: '))
    flag = n

    if flag != 999:
        cont += 1
        soma += n
print(f'Foram lidos {cont} valores e sua soma é {soma}.')