'''
Criar um programa para aprovar um emprestimo bancario:
- Deve perguntar o valor da casa;
- O salário do comprador;
- E em quantos anos ele pretende pagar.

A prestação não pode esceder 30% do saláio do comprador ou o emprestimo é negado.
'''

# Secao de funções e procedimentos

'''
def valordacasa():
    valorcasa = float(input('Qual o valor da casa: R$ '))
    return valorcasa

def salariodocomprador():
    salario = float(input('Qual é seu salário bruto: R$ '))
    return salario

def anospagando():
    tempo = float(input('Em quantos pretende quitar a casa: '))
    return tempo

def calculaprestacao(x, y): # X é o valor da casa e Y os anos de pagamento
    Nparcelas = 12*y
    prestacao = x/Nparcelas
    return prestacao

def Aprovado(x, y): # Com x sendo a prestacao e y 30% do salario do comprador.
    return x < y or False
# Programa Principal

valorcasa = valordacasa()
salario = salariodocomprador()
tempo = anospagando()

prestacao = calculaprestacao(valorcasa, tempo)

limiteprestacao = 0.3*salario

print(f'O emprestimo foi aprovado? {Aprovado(prestacao, limiteprestacao)}')

'''

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Quanto voce recebe? R$ '))
anos = float(input('Em quantos anos pretende quitar a casa? '))

parcela = casa/(anos*12)
limite = 0.3*salario

if parcela > limite:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo APROVADO!')
    print(f'A parcela sera de `R$ {parcela:.2f} mensais')
