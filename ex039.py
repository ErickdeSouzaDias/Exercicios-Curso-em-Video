'''
Alistamento militar
Deve solicitar:
- O ano de nascimento;
- E o ano atual.

Deve informar:
- Se vai se alistar;
- Se esta na hora exata;
- Ou se passou da hora;
- Deve tambem informar o tempo que falta;
- Ou que passou.
'''
from datetime import date

def cabecalho():
    print(40*'*')
    print('\t\t\tStatus alistamento')
    print(40*'*')

def informacoes():
    ano_atual = date.today().year
    nascimento = int(input('Em qual ano voce nasceu? '))
    return ano_atual - nascimento, ano_atual

cabecalho()
idade, ano_atual = informacoes()

if idade < 18:
    print(f'Voce possui {idade} anos, ainda nao e hora de se alistar.')
    print(f'Faltam {18-idade} anos para seu alistamento.')
    print(f'Voce deve se alistar {ano_atual+(18-idade)}.')
elif idade > 18:
    print(f'Voce possui {idade}anos, ja passou da hora de se alistar.')
    print(f'Passaram {idade - 18} anos do seu alistamento.')
    print(f'Voce devia ter se alistado em {ano_atual-(idade-18)}.')
else:
    print(f'Voce deve se alistar nesse ano, voce possui {idade}.')
print('\n')
print('Regularize sua situacao de acordo com o informado acima.')