# Fazer um programa que jogue Jokenpo comigo.
from random import choice
from time import sleep

print('{:*^40}'.format('Jokenpo'))

player = int(input('Opcoes:\n1 - Pedra\n2 - Papel\n3 - Tesoura\nSua escolha: '))
if player == 1:
    player = 'Pedra'
elif player == 2:
    player = 'Papel'
elif player == 3:
    player = 'Tesoura'
computador = choice(['Pedra', 'Papel', 'Tesoura'])
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print(21*'-=')
if player == computador:
    print(f'Player jogou {player} e computador jogou {computador}.')
    print('Deu empate!')
else:
    if player == 'Pedra' and computador == 'Papel':
        print(f'Player jogou {player} e computador jogou {computador}.')
        print('O computador ganhou!')
    elif player == 'Pedra' and computador == 'Tesoura':
        print(f'Player jogou {player} e computador jogou {computador}.')
        print('O player ganhou!')
    elif player == 'Papel' and computador == 'Pedra':
        print(f'Player jogou {player} e computador jogou {computador}.')
        print('O player ganhou!')
    elif player == 'Papel' and computador == 'Tesoura':
        print(f'Player jogou {player} e computador jogou {computador}.')
        print('O computador ganhou!')
    elif player == 'Tesoura' and computador == 'Pedra':
        print(f'Player jogou {player} e computador jogou {computador}.')
        print('O computador ganhou!')
    elif player == 'Tesoura' and computador == 'Papel':
        print(f'Player jogou {player} e computador jogou {computador}.')
        print('O player ganhou!')
    else:
        print('JOGADA INVALIDA!')
print(21*'-=')