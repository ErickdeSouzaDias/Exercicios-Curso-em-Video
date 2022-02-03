"""
    Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

opcao = ''
while opcao != '5':
    while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':

        opcao = str(input('''Opções:
        [1] - Somar
        [2] - Multiplicar
        [3] - Maior
        [4] - Novos números
        [5] - Sair do programa
        
        Sua escollha: ''')).upper().strip()[0]

        if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
            print('Opção inválida! Tente novamente...')

    if opcao == '1':
        print(f'A soma de {num1} + {num2} é {num2+num1}.')
    elif opcao == '2':
        print(f'O produto de {num1} X {num2} é {num2*num1}.')
    elif opcao == '3':
        if num1 > num2:
            print(f'o número {num1} é maior que {num2}.')
        elif num2 > num1:
            print(f'O número {num2} é maior que {num1}.')
        else:
            print('Os dois números digitados são iguais!')
    elif opcao == '4':
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
    elif opcao == '5':
        print('************TCHAU!!!************')
        break
    sleep(3)
    opcao = ''
print('Programa finalizado!')