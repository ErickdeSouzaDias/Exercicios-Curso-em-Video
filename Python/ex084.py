"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
cadastros = list()
Nome_maior, Nome_menor = list(), list()
cont = 0

while True:
    dados = list()
    cont += 1
    dados.append(str(input('Qual seu nome: ')))
    dados.append(float(input('Qual seu peso: ')))
    cadastros.append(dados)

    if cont == 1:
        maior = menor = dados[1]
    else:
        if dados[1] >= maior:
            maior = dados[1]
            Nome_maior.append([dados[0]])
        if dados[1] <= menor:
            menor = dados[1]
            Nome_menor.append([dados[0]])
            
    del dados
    Continuar_Programa = str(input('Deseja continuar: [S/N] ')).upper().strip()[0]
    if Continuar_Programa == "N":
        break

print(f'Foram cadastradas {cont} pessoas.')
print(f'O menor peso lido foi de {menor} de {Nome_menor}.')
print(f'O maior peso lido foi de {maior} de {Nome_maior}.')
