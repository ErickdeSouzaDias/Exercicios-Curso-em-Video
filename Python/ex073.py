"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

ranking = ('Ranking CBF 2022', 'Flamengo', 'Palmeiras', 'Atlético - MG', 'Grêmio', 'Athletico', 'Santos',
           'São Paulo', 'Internacional', 'Fluminense', 'Corinthians', 'Fortaleza', 'Bahia', 'Ceára',
           'Cruzeiro', 'América', 'Atlético - GO', 'Chapecoense', 'Botafogo', 'Vasco da Gama', 'RB Bragantino')

print(f'{ranking[0]:-^30}', 'Primeiros 5 colocados:', sep="\n")
for pos, time in enumerate(ranking[1:6]):
    print(f'{pos+1:<} - {time:>}')
print()

print('Últimos 4 colocados:')
for pos, time in enumerate(ranking[17:len(ranking)]):
    print(f'{ranking.index(time):<} - {time}')
print()

print('Times em ordem alfabética:')
for time in sorted(ranking):
    print(time)
print()

print(60*'-')
print(f'A chapecoense entá na {ranking.index("Chapecoense")}º do ranking.')
print(60*'-')
