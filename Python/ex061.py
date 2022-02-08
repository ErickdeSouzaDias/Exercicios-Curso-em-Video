"""
    Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
    mostrando os 10 primeiros termos da progressão usando a estrutura while.

"""
print(30*'#')
print(f'{"Progressão aritmética":^30}')
print(30*'#')

p = int(input('Qual o primeiro termo: '))
n = int(input('Qual a razão: '))
pa = p

cont = 1
print(f'{pa} ', end="")
while cont <= 9:
    pa += n
    cont += 1
    print(f'-> {pa} ',end="")
print('-> FIM')
