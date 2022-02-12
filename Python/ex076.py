"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma
tabular.
"""

produtos = ('Arroz', 2.77, 'Feijão', 10.50, "Milho", 3.00, 'Azeite', 2.90, 'Barraca', 359.00,
            'Tigela de vidro', 8.59, 'Filtro de barro', 190.00)

print(45*'=')
print(f'{"Listagem de produtos":^45}')
print(45*'=')


for item in produtos:
    if type(item) is str:
        print(f"{item :.<35}", end="")
    else:
        print(f'R$ {item:>7.2f}')
print(45*'=')
