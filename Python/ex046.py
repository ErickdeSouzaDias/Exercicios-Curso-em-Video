'''
Um programa que mostre na tela uma contagem regresiva
para a queima de fogos de artificio
Deve comecar em 10 e terminar em 0 com uma pausa de 1 segundo entre
os a contagem.
'''

azul_claro = '\033[1;104m '
preto = '\033[1;30m '
vermelho = '\033[1;31m '

from  time import sleep

print(azul_claro)
for c in range(10,-1,-1):
    print(preto)
    print('\t{:=^20}\t'.format(c))
    sleep(0.5)
print(vermelho)
print('\n\t BOOM! BOOM! POOH!')