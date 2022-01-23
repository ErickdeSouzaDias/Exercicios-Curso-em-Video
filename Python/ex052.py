'''
    Descobrir se um numero e primo.

    Fazer a leitura de uma valor

'''
amarelo = '\033[1;33m'
vermelho = '\033[1;31m'
reset = '\033[0;0m'
n = int(input('Informe um numero: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print(amarelo,c, end=' ')
        cont += 1
    else:
        print(vermelho,c, end=' ')
print('\n',reset)
print(f'O numero {n} foi divisivel po {cont} vezes.')
if n == 1:
    print('O nuemro 1 e divisivel apenas por ele mesmo.')
elif cont == 2:
    print('e por isso ele E PRIMO')
else:
    print('E por isso ele NAO E PRIMO.')
