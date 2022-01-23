'''
    Fazer um programa que leia o primeiro termo e a razao de uma
    PA e mostre seus 10 primeiros termos.
'''
print(28*'=')
print('\t10 TERMOS DE UMA PA')
print(28*'=')
a1 = int(input('Qual o primeiro termo: '))
r = int(input('Qual a razao: '))
last = int((a1+(a1+(10-1)*r)*1))
for c in range(a1, last, r):
    if c != last-1:
        print(f'{c}',end='->')
    else:
        print(f'{c}', end='')
