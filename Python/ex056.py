"""
    Desenvolva um programa que leia o nome, idade e sexo de
    4 pessoas. No final do programa, mostre: a média de idade
    do grupo, qual é o nome do homem mais velho e quantas mulheres
    têm menos de 20 anos.

"""
# 1 Primeiro ler os valores em laço
# 2 Calcular a media da idade do grupo
# 3 Guardar o nome do homem mais velho
# 4 Guardar quantas mulheres tem menos de 20 anos

media = 0
homem_mais_velho = 0
mulher_abaixo_de_vinte = 0
for c in range(1, 5):
    nome = str(input(f'O nome da {c}º pessoa: '))
    idade = int(input(f'Qual sua idade, {nome}: '))
    sexo = str(input('Qual seu sexo:[F/M] ')).upper().strip()
    media += idade

    if sexo[0] == 'M' and c == 1:
        homem_mais_velho = idade
    elif sexo[0] == 'M' and idade > homem_mais_velho:
        homem_mais_velho = nome

    if sexo[0] == 'F' and idade < 20:
        mulher_abaixo_de_vinte += 1

media = media/4

print(f'A media das idades lidas é {media:.2f}.')
print(f'O homem mais velho se chama, {nome}!')
print(f'{mulher_abaixo_de_vinte} pessoas do sexo feminino possuem menos de 20 anos!')

