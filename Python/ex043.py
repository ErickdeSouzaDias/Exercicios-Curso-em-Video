def separador():
    print(20*'-=')

def cabecalho():
    print(40*'*')
    print('\t\tCalculadora de IMC')
    print(40*'*')

class Pessoa:
    altura = 0
    peso = 0
    imc = 0

pessoa1 = Pessoa()

cabecalho()

pessoa1.altura = float(input('Digite sua altura: '))
pessoa1.peso = float(input('Digite seu peso: '))
pessoa1.imc = pessoa1.peso/(pessoa1.altura**2)

print(f'Seu IMC eh de {pessoa1.imc:.2f}.')

if pessoa1.imc < 18.5:
    print('Voce esta abaixo do peso!')
    separador()
elif pessoa1.imc < 25:
    print('Voce esta no peso ideal!')
    separador()
elif pessoa1.imc < 30:
    print('Voce esta em sobrepeso!')
    separador()
elif pessoa1.imc < 40:
    print('Voce esta com obesidade!')
    separador()
else:
    print('Voce esta com obesidade morbida!')
    separador()
