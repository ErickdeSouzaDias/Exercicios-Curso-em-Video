"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print(30 * '-=')
print(f'{"Caixa eletrónico":^60}')
print(30 * '-=')
valor = int(input('Qual o valor a ser sacado: '))

cedula_cinquenta = cedula_vinte = cedula_dez = cedula_um = 0
while True:
    if valor < 0:
        print('Valor inválido!')
    if valor >= 1000:
        valor -= 50
        cedula_cinquenta += 1
    elif valor >= 100:
        valor -= 50
        cedula_cinquenta += 1
    elif valor >= 50:
        valor -= 50
        cedula_cinquenta += 1
    elif valor >= 20:
        valor -= 20
        cedula_vinte += 1
    elif valor >= 10:
        valor -= 10
        cedula_dez += 1
    elif valor >= 1:
        valor -= 1
        cedula_um += 1
    else:
        break
if valor == 0:
    print(60*'-')
    print(f'{"Saque":^60}')
    print(60*'-')
    print(f'{cedula_cinquenta} cédulas de cinquenta reais.'if cedula_cinquenta > 0 else "")
    print(f'{cedula_vinte} cédulas de vinte reais.'if cedula_vinte > 0 else "")
    print(f'{cedula_dez} cédulas de dez reais.'if cedula_dez > 0 else "")
    print(f'{cedula_um} cédulas de um real.'if cedula_um > 0 else "")
else:
    print('Sessão encerrada.')
print(30*'-=')
