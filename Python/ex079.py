"""
Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados, em
ordem crescente.
"""

numeros = list()
while True:
    op = ''
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Numero adicionado com sucesso!')
    else:
        print('Número repetido. Não foi adicionado a lista!')
    while 'S' != op != 'N':
        op = str(input('Deseja continuar? ')).strip().upper()[0]
        if op == 'S':
            continue
        elif op == 'N':
            break
        else:
            print('Opção inválida!')
    if op == 'N':
        break
numeros.sort()
print(f'Os numeros digitados foram {numeros}.')
