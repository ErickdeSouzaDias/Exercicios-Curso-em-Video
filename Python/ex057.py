"""
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
    ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter
    um valor correto.
"""

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual seu sexo: [M/F] ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Valor inválido! Tente novamente.')
