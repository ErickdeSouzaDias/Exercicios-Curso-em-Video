"""
     Escreva um programa que faça o computador "pensar" em um número inteiro
     entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
     escolhido pelo computador. O programa deverá escrever na tela se o usuário
     venceu ou perdeu.
"""
print(60*'=')
print('Irei pensar em um número, você consegue descobrir qual é?')
print(60*'=')
from random import randint
sorteado = randint(1,5)
palpite = int(input('Em qual número estou pensando entre 1 e 5? '))
if palpite == sorteado:
    print('PARABÉNS! Você acertou.')
else:
    print(f'Você errou! Eu estava pensando no {sorteado}.')
