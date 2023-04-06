# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #036
# ---------------------------


valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário? '))
ano = int(input('Em quantos anos será pago? '))
prestacao = valor / ano
print('A prestação mensal vale {}R${:.2f}{}'.format('\033[32m', prestacao, '\033[m'))
if prestacao > 30/100*salario:
    print('{}O empréstimo foi negado! Excedeu 30% do salário!{}'.format('\033[31m', '\033[m'))
