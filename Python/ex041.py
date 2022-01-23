'''
Programa que leia o ano de nascimento de um atlteta e calcule sua idade;
Classificar o atleta como:
- Ate 9 anos: Mirim
- Ate 14 anos: Infantil
- Ate 19 anos: Junior
- Ate 25 anos: Senior
- Acima de 25 anos: Master
'''

from datetime import date

atual = date.today().year

nascimento = int(input('Em qual ano voce nasceu? '))

idade = atual - nascimento

if 9 >= idade:
    print(f'O atleta possui {idade}.')
    print('Entao ele e um atleta MIRIM')
elif 9 < idade <= 14:
    print(f'O atleta possui {idade}.')
    print('Entao ele e um atleta INFANTIL.')
elif 14 < idade <= 19:
    print(f'O atleta possui {idade}.')
    print('Entao ele e um atleta JUNIOR')
elif 19 < idade <= 25:
    print(f'O atleta possui {idade}.')
    print('Entao ele e um atleta SENIOR')
else:
    print(f'O atleta possui {idade}.')
    print('Entao ele e um atleta MASTER')


