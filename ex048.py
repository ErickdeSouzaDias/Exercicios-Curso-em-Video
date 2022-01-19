#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 09:13:37 2022

@author: erickdsd

Faça um programa que calcule a soma entre todos os números que são múltiplos
de três e que se encontram no intervalo de 0 até 500.

"""

print('Números pares multiplos de 3 entre 1 e 500:\n')
soma = 0
cont = 0
for n in range(0,500,3):
    if n%2==1:
        cont += 1
        soma += n
print(f'A soma de todos os {cont} valores solicitados é {soma}.')


