"""
    Crie um programa que leia vários números inteiros pelo teclado.
    No final da execução, mostre a média entre todos os valores e
    qual foi o maior e o menor valores lidos. O programa deve perguntar
     ao usuário se ele quer ou não continuar a digitar valores.
"""

n = cont = soma = maior = menor = media = 0
while n != 999:
    n = int(input('Digite qualquer valor [999 - Sair]: '))
    flag = n

    if flag != 999:
        cont += 1
        soma += n
        if cont == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n

    media = soma/cont
    op = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if op == 'N':
        n = 999
print(f'Foram digitados {cont} numeros.')
print(f'O maior valor lido foi {maior}.')
print(f'O menor valor lido foi {menor}.')
print(f'A média dos valores lidps foi {media:.2f    }.')