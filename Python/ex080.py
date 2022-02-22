"""Crie um programa onde o usuário possa digitar cinco valores
numéricos e cadastre-os em uma lista, já na posição correta de
inserção (sem usar o sort()). No final, mostre a lista ordenada
na tela.
"""

# Fazer leitura de 5 valores
    # Urilizar o laço for
# Ordenar valores após a leitura
    # Usar estrutura condicional
# Exibir a lista

lista = list()
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print('Valor adicionado na posição {} da lista.'.format(pos))
                break
            pos += 1
print(f'Os valores digitados em ordem são {lista}.')
