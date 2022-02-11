"""
 Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
 quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
 no final do jogo.
"""

from random import randint
vitorias = 0

print(12*'=-')
print('Vamos jogar Par ou Impar')
print(12*'=-')

while True:
    n = -1
    while n < 0 or n > 10:
        n = int(input('Digite um valor: '))
        if not(-1 < n < 11):
            print('Valor invalido! O número digitado deve estar entre 0 e 10.')

    op = ''
    while op != 'P' and op != 'I':
        op = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
        if op != 'P' and op != 'I':
            print('Opção inválida! Digite "P" para PAR ou "I" para IMPAR.')

    pc = randint(0, 10)

    print(f'Você jogou {n} e o computador {pc}. Total de {n+pc} DEU {"PAR" if (n+pc)%2==0 else "IMPAR"}')
    print(24*'-')
    if (n+pc) % 2 == 0 and op == 'P':
        print('Você ganhou! Vamos jogar novamente.')
        vitorias += 1
    elif (n+pc) % 2 == 1 and op == 'I':
        print('Você ganhou! Vamos jogar novamente.')
        vitorias += 1
    elif (n+pc) % 2 == 0 and op == 'I':
        print(f'GAME OVER! Você venceu {vitorias} vezes.')
        break
    elif (n+pc) % 2 == 1 and op == 'P':
        print(f'GAME OVER! Você venceu {vitorias} vezes.')
        break
    print(24 * '-')
