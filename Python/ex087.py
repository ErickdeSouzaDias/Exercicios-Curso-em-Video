#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 19:05:30 2023

@author: erick
"""

# Aprimore o desafio anterior, mostrando no final:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares, soma_terceira_coluna, maior_segunda_linha, cont = 0, 0, 0, 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para posição {l+1}x{c+1}: '))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            soma_terceira_coluna += matriz[l][c]
        if matriz[l][c] == matriz[1][c]:
            if cont == 0:
                maior_segunda_linha = matriz[l][c]
                cont += 1
            elif matriz[1][c] > maior_segunda_linha:
                maior_segunda_linha = matriz[1][c]

print('Matriz'.center(30, '='))
        
for l in range(0, 3):
    for c in range(0, 3):
        print('[', f'{matriz[l][c]}'.center(4), ']', end='')
    print()

print('Informativo'.center(30, '='))
# A soma de todos os valores pares digitados;
print(f'A soma dos valores pares digitados é {soma_pares}.')
# A soma dos valores da terceira coluna;
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')
# O maior valor da segunda linha
print(f'O maior valor digitado na segunda linha é {maior_segunda_linha}.')
print('='*30)
