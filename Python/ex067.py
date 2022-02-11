"""
 Faça um programa que mostre a tabuada de vários números, um de cada vez,
 para cada valor digitado pelo usuário. O programa será interrompido
 quando o número solicitado for negativo.
"""

while True:
    n = int(input("Qual tabuada deseja visualizar: "))
    if n < 0:
        break

    print(32 * '#')
    for c in range(0, 11):
        print(f'#         {n} X {c:^3} = {n*c:^3}', end="")
        print(7*' ', '#')
    print(32 * '#')
print(32*'#')
print("Programa finalizado com sucesso!")
print(32*'#')
