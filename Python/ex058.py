"""
     Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um
     número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
     até acertar, mostrando no final quantos palpites foram necessários
     para vencer.
"""

from random import randint
sorteado = randint(1,10)
tentativas = 0
palpite = 0

print(60*'=')
print('Irei pensar em um numero! Você consegue descobrir em qual?')
print(60*'=')

while palpite != sorteado:
    palpite = int(input('Em qual número estou pensando entre 1 e 10? '))
    if palpite == sorteado:
        print(f'Parabéns você acertou! Foram necessárias {tentativas} tentativas.')
    else:
        tentativas += 1
        if palpite < sorteado:
            print(f'Mais! tente novamente!')
        elif palpite > sorteado:
            print('Menos! tente novamente!')
