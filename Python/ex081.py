"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = list()  # Cria a variável composta do tipo lista.
print(30*'=-')  # Um frufruzinho

while True:
    op = ''
    lista.append(int(input('Digite um número: ')))  # Adição de elementos a lista.
    while 'S' != op != 'N':  # Validação de continuidade do programa.
        op = str(input('Quer continuar?[S/N] ')).upper().strip()[0]  # Pergunta se o user quer continuar no programa.
        if 'S' != op != 'N':
            print('Opção Inválida! Tente Novamente')

    if op == 'S':
        continue
    if op == 'N':
        break
# Analíse da lista.
print(f'Foram digitados {len(lista)} números.')
print(f'A lista é {sorted(lista, reverse = True)}.')
print(f'O valor 5 foi digitado na {lista.index(5)}ª posição.' if 5 in lista
      else 'O valor 5 não foi digitado.')
