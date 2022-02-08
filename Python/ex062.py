"""

    Melhore o DESAFIO 61, perguntando para o usuário se ele quer
    mostrar mais alguns termos. O programa encerrará quando ele
    disser que quer mostrar 0 termos.

"""

print(30*'#')
print(f'{"Progressão aritmética":^30}')
print(30*'#')

p = int(input('Qual o primeiro termo: '))
n = int(input('Qual a razão: '))
opcao = int(input('Quantos termos deseja mostrar: '))
pa = p

termos = 0
cont = 1
while cont <= opcao or opcao != 0:
    print(f'{pa}',end="")
    print(' -> ' if cont < opcao else ' -> PAUSA', end="")
    pa += n
    cont += 1
    termos += 1
    if cont > opcao:
        cont = 1
        opcao = int(input('\n\nDeseja mostrar mais quantos termos? [0 - Para sair]: '))
print(f'Ao todo foram mostrados {termos} termos.')
print(f'De uma progressão aritmética que começa em {p} e possui razão {n}.')
