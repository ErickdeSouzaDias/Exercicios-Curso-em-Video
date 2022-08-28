"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
crescente. """

pares = []
impares = []
valores = [pares, impares]

for posicao in range(1, 8):
    numero = int(input(f'Digite o {posicao}º número: '))

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(20*'=*')

print(f'Os valores pares digitados foram {sorted(pares)}.')
print(f'Os valores impares digitados foram {sorted(impares)}.')
