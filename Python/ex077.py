"""
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.
"""

palavras = ('Listagem', 'Jardinagem', 'Brincadeira', 'Confete', 'Santa Catarina',
            'Cafe')

for palavra in palavras:
    print(f'A palavra {palavra} contém as vogais:', end="")
    if palavra.count('a') > 0:
        print('a', end=" ")
    if palavra.count('e') > 0:
        print('e', end=" ")
    if palavra.count('i') > 0:
        print('i', end=" ")
    if palavra.count('o') > 0:
        print('o', end=" ")
    if palavra.count('u') > 0:
        print('u', end=" ")
    print()
