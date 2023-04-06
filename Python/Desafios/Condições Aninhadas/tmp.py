# Desafio 1
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário? '))
ano = int(input('Em quantos anos será pago? '))
prestacao = valor / ano
print('A prestação mensal vale {}R${:.2f}{}'.format('\033[32m', prestacao, '\033[m'))
if prestacao > 30/100*salario:
    print('{}O empréstimo foi negado! Excedeu 30% do salário!{}'.format('\033[31m', '\033[m'))


# Desafio 2
dec = int(input('Digite um número em decimal: '))
print('Para qual base deseja fazer a conversão? ')
opt = int(input('1: Binário\n2: Octal\n3: Hexadecimal\n'))
if opt == 1:
    print('{} Em binário é \033[34m{}\033[m'.format(dec, bin(dec)))
elif opt == 2:
    print('{} Em octal é \033[34m{}\033[m'.format(dec, oct(dec)))
elif opt == 3:
    print('{} Em hexadecimal é \033[34m{}\033[m'.format(dec, hex(dec)))
else:
    print('{}Opção inválida!{}'.format('\033[31m', '\033[m'))


# Desafio 3
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
if x > y:
    print('O primeiro é maior')
elif y > x:
    print('O segundo é maior')
else:
    print('Não existe valor maior, os dois são iguais')


# Desafio 4
from datetime import date
ano_nasc = int(input('Você nasceu em que ano? '))
idade = date.today().year - ano_nasc
if idade < 18:
    print('\033[1mVocê ainda vai ser dispensado!\033[m Falta {} ano(s)!\n'.format(18-idade))
elif idade == 18:
    print('\033[1mHora de ser dispensado!\033[m\n')
else:
    print('\033[1mJá foi dispensado!\033[m Passou {} ano(s)\n'.format(idade-18))
print('\033[4;33mAlistamento obrigatório é um absurdo!\033[m')
print('\033[1;31mPelo fim das práticas obsoletas do Exército brasileiro!\033[m')


# Desafio 5
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2
if m >= 7:
    print('Média: {:.2f} | {}APROVADO!{}'.format(m, '\033[32m', '\033[m'))
elif m < 5:
    print('Média: {:.2f} | {}REPROVADO!{}'.format(m, '\033[31m', '\033[m'))
else: # m >= 5 and m < 7
    print('Média: {:.2f} | {}RECUPERAÇÃO!{}'.format(m, '\033[33m', '\033[m'))


# Desafio 6
from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nasc
if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JÚNIOR')
elif idade == 20:
    print('SÊNIOR')
elif idade > 20:
    print('MASTER')
else:
    print('Idade inválida')


# Desafio 7
a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))
if (a < b + c) and (b < a + c) and (c < a + b):
    if (a == b) and (b == c):
        print('Será formado um triângulo equilátero')
    elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
        print('Será formado um triângulo isósceles')
    else:
        print('Será formado um triângulo escaleno')
else:
    print("Não é possível formar um triângulo com esses lados")


# Desafio 8
altura = float(input('Digite sua altura (m): '))
peso = float(input('Digite seu peso: (kg): '))
imc = peso / altura**2
if imc < 18.5:
    print('IMC: {:.1f} | Abaixo do peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('IMC: {:.1f} | Peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('IMC: {:.1f} | Sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('IMC: {:.1f} | Obesidade'.format(imc))
else:
    print('IMC: {:.1f} | Obesidade mórbida'.format(imc))


# Desafio 9
valor = float(input('Preço normal: '))
cond = int(input('1: À vista no dinheiro/cheque\n2: À vista no cartão:\n3: Até 2x no cartão\n4: 3x ou mais no cartão:\n'))
if cond == 1:
    print('O valor a ser pago é de R${:.2f}'.format(90/100*valor))
elif cond == 2:
    print('O valor a ser pago é de R${:.2f}'.format(95/100*valor))
elif cond == 3:
    print('O valor a ser pago é de R${:.2f}'.format(valor))
elif cond == 4:
    print('O valor a ser pago é de R${:.2f}'.format(120/100*valor))
else:
    print('Opção inválida')


# Desafio 10
from random import randint
from time import sleep
print('\033[34m-=-\033[m'*15)
print('{}{} JOKENPÔ {}{}'.format('\033[1;34m', '=='*9, '=='*9, '\033[m'))
print('\033[34m-=-\033[m'*15)
comp = randint(1, 3)
print('\033[33mPEDRA = 1 | PAPEL = 2 | TESOURA = 3\033[m')
user = int(input('\033[35mFAÇA SUA ESCOLHA: \033[m'))
print('\033[3;34mPROCESSANDO... \033[m')
sleep(1.5)
if comp == 1:
    if user == 1:
        print('\033[36mEMPATOU!\033[m')
    elif user == 2:
        print('\033[32mVOCÊ VENCEU!\033[m')
    elif user == 3:
        print('\033[31mVOCÊ PERDEU!\033[m')
    else:
        print('\033[1mESCOLHA INVÁLIDA!\033[m')
elif comp == 2:
    if user == 1:
        print('\033[31mVOCÊ PERDEU!\033[m')
    elif user == 2:
        print('\033[36mEMPATOU!\033[m')
    elif user == 3:
        print('\033[32mVOCÊ VENCEU!\033[m')
    else:
        print('\033[1mESCOLHA INVÁLIDA!\033[m')
elif comp == 3:
    if user == 1:
        print('\033[32mVOCÊ VENCEU!\033[m')
    elif user == 2:
        print('\033[31mVOCÊ PERDEU!\033[m')
    elif user == 3:
        print('\033[36mEMPATOU!\033[m')
    else:
        print('\033[1mESCOLHA INVÁLIDA!\033[m')

