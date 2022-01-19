#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 09:46:08 2022

@author: erickdsd

Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.

"""

n = int(input('Digite umnumero para ver sua tabuada: '))
for c in range(0,11,1):
    print(f'{n} x {c} = {n*c}')


