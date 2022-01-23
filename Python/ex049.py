'''
    Fazer um programa que mostre a tabuada de um numero escilhido pelo usuario
'''

n = int(input('Digite um numero: '))
for c in range(0, 11):
    print(f'{n} X {c} = {n*c}')
