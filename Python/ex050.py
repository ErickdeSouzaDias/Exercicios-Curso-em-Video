'''
    Fazer a leitura de 6 valores via teclado e informa a soma apenas dos pares.
'''

soma = 0
for c in range(1,7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos numeros pares digitados e {soma}.')