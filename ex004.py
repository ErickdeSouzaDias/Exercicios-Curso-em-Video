''''
Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

palavra = input('Digite algo: ')

print(f'O tipo primitivo deste valor é: {type(palavra)}')
print(f'Só tem espaços? {palavra.isspace()}.')
print(f'É um número? {palavra.isnumeric()}.')
print(f'É alfabético? {palavra.isalpha()}.')
print(f'É alfanúmerico? {palavra.isalnum()}')
print(f'Está em maiúsculas? {palavra.isupper()}')
print(f'Está em minúsculas? {palavra.islower()}')
print(f'Está capitalizada? {palavra.istitle()}')
