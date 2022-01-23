l1 = int(input('Digite o valor do lado 1 do triangulo: '))
l2 = int(input('Digite o valor do lado 2 do triangulo: '))
l3 = int(input('Digite o valor do lado 3 do triangulo: '))

print(f'Com os segmentos {l1}, {l2} e {l3}.')
if l1 + l2 > l3 and l2 +l3 > l1 and l1 + l3 > l2:
    print('Pode se formar um traingulo.')
    if l1 == l2 and l2 == l3:
        print('O triangulo e EQUILATERO.')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('O triangulo e ISOCELES.')
    elif l1 != l2 != l3:
        print('O triangulo e ESCALENO.')
else:
    print('Nao se pode formar um triangulo.')
