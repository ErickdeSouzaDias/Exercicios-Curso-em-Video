#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:16:02 2023

@author: erick
"""

# Crie um programa que crie uma matriz de dimensão 3x3 e preen
# cha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para posição {l+1}x{c+1}: '))
        
for l in range(0, 3):
    for c in range(0, 3):
        print('[', f'{matriz[l][c]}'.center(4), ']', end='')
    print()