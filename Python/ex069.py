"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""

print(30*'#')
print(f'{"Cadastro":^30}')
print(30*'#')

MaiorDe18 = homens = mulherMenos20 = 0
sexo = op = ''
idade = -1

while True:
    print(30*'-')
    while idade > 150 or idade < 0:
        idade = int(input('Qual sua idade: '))
        if idade > 150 or idade < 0:
            print("Opção inválida! Tente novamente.")

    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()[0]
        if sexo != 'M' and sexo != 'F':
            print("Opção inválida! Tente novamente.")

    if idade >= 18:
        MaiorDe18 += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F':
        if idade <= 20:
            mulherMenos20 += 1

    while op != 'S' and op != 'N':
        op = str(input('Deseja continuar: [S/N] ')).upper().strip()[0]
        if op != 'S' and op != 'N':
            print("Opção inválida! Tente novamente.")

    if op == 'N':
        break
    else:
        idade = -1
        sexo = ''
        op = ''
        continue
print(30*'-')

print('Foram cadastrados(as):')
print(f'Maiores de 18 anos: {MaiorDe18}')
print(f'São homens: {homens}')
print(f'Mulhres com menos de 20 anos: {mulherMenos20}')
print(30*'-')