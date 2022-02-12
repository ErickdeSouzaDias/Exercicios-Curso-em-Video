"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
por extenso.
"""

numeros = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito',
           'Dezenove', 'Vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {numeros[numero]}.')
        while True:
            op = str(input('Deseja continuar: ')).upper().strip()[0]
            if op == 'S' or op == 'N':
                break
            else:
                print('Opção inválida! Tente novamente.')
        if op == 'S':
            continue
        else:
            break
    else:
        print('Número inválido! Tente novamente.')
