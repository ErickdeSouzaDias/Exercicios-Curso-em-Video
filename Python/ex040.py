'''
Fazer um programa que leia duas notas;
calcule a media
Informe:
- media < 5 e reprovado.
- media >= 5 e media <= 6.9 e recuperacao
- media >= 7 e aprovado
'''

n1 = float(input('Qual a primeira nota: '))
n2 = float(input('Qual a segunda nota: '))
media = (n1+n2)/2
print(f'Sua meida e {media:.2f}.')
if media < 5:
    print('Aluno REPROVADO!')
elif media >= 5 and media <= 6.9:
    print('Aluno em RECUPERACAO!')
elif media >= 7:
    print('Aluno APROVADO!')
