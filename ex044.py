# Fazer um programa que leia:
# O valor de um produto;
# E o meio de pagamento.
# E a partir disto, calcular o valor final do produto.

# A vista dinheiro/Cheque: 10% de desconto;
# A vista no cartao 5% de desconto;
# Em ate 2x no cartao preco normal
# 3x ou mais no cartao 20% de juros
def separador():
    print(20*'-=')

class item:
    pass

produto = item()

produto.preco = float(input('Qual o valor do produto: R$ '))
print('''Forma de pagamento:\n1 - A vista dinheiro/Cheque\n2 - A vista no cartao
3 - Em 2x no cartao\n4 - 3x ou mais no cartao''')
produto.pagamento = int(input('Qual a forma de pagamento: '))
separador()

if produto.pagamento == 1:
    print('Voce obteve 10% de desconto!')
    print(f'O valor final do produto eh R$ {produto.preco-(produto.preco*0.1)}')
    separador()
elif produto.pagamento == 2:
    print('Voce obteve 5% de desconto!')
    print(f'O preco final do produto eh R$ {produto.preco-(produto.preco*0.05)}')
    separador()
elif produto.pagamento == 3:
    print('Voce nao obteve descontos.')
    print(f'O valor final do produto eh R$ {produto.preco}.')
elif produto.pagamento == 4:
    produto.parcela = int(input('Quantas vezes: '))
    print('Voce pagara 20% de juros!')
    print(f'O parcelamento sera {produto.parcela}x R$ {(produto.preco + (produto.preco * 0.2)) / produto.parcela}.')
    print(f'O valor final do produto eh de R$ {produto.preco + (produto.preco * 0.2)}')
print('Volte sempre!')