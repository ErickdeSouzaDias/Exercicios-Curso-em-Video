'''
    Fazer s soma dos impares multiplos de 3 de 1 a 500
'''
soma = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        soma += c
print(f'A soma dos numeros impares multiplos de 3 entre 1 e 500 e {soma}.')