"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
temp = list()
princ = list()
maior = menor = 0

while True:
    temp.apend(str(input('Nome: ')))
    temp.apend(float(input('Peso: ')))
    if len(temp) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior: