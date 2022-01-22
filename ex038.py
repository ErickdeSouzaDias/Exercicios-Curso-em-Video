n = float(input('Digite um numero: '))
m = float(input('Digite outro numero: '))

if n > m:
    print(f'{n} e maior que {m}.')
elif m > n:
    print(f'{m} eh maior que {n}.')
else:
    print(f'{n} e igual a {m}.')
