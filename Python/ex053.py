"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA
MARATONA.
"""
frase = input('Digite uma frase: ').replace(' ', '').upper().strip()
inverso = ''
for c in range(len(frase) -1, -1, -1):
    inverso += frase[c]
print(f'O inverso de {frase} é {inverso}.')

if inverso == frase:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')

