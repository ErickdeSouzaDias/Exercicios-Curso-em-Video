"""
 Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""

print(30*'-#')
print(f'{"Mercado Kcire":^60}')
print(30*'-#')

totalCompra = Maisde1000 = maisBarato = 0
nomeMaisBarato = ' '
cont = 0
while True:
    print(60*'-')
    cont += 1
    op = ' '

    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    totalCompra += preco

    if preco > 1000:
        Maisde1000 += 1
    if cont == 1:
        maisBarato = preco
    else:
        if preco < maisBarato:
            nomeMaisBarato = nome
            maisBarato = preco

    while op not in 'SN':
        op = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(60*'-')
print(f'O total da compra foi de R$ {totalCompra:.2f}.')
print(f'Ao todo comprou-se {Maisde1000} produtos acina de MIL REAIS.')
print(f'O produto mais barato foi {nomeMaisBarato} custando R$ {maisBarato:.2f}.')
