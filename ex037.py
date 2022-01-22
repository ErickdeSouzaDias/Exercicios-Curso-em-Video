'''
Receber um valor interiro de entrada e escolher entre 3 opçoes de conversao de base
1 - binario
2 - Octal
3 - Hexadecimal
'''

n = int(input('Digite um numero inteiro: '))
opcao = int(input('Converter para:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\nEscolha:'))

if opcao == 1:
    print(f'O numero {n} em DECIMAL eh equivalente a {str(bin(n))[2:]} em BINARIO.')
elif opcao == 2:
    print(f'O numero {n} em DECIMAL eh equivalente a {str(oct(n))[2:]} em OCTAL.')
elif opcao == 3:
    print(f'O numero {n} em DECIMAL eh equivalente a {str(hex(n))[2:]} em HEXADECIMAL.')
else:
    print('Opcao invalida!')