l1 = float(input('Digite o primeriro segmento: '))
l2 = float(input('Digite o segundo segmento: '))
l3 = float(input('Digite o terceiro segmento: '))

if l1 +  l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print(f'Com os segmentos {l1}, {l2}, {l3}.')
    print('Pode se formar im triangulo.')
else:
    print(f'Com os segmentos {l1}, {l2}, {l3}.')
    print('Nao e possivel formar um triangulo.')