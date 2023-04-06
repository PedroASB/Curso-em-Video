# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #034
# ---------------------------


salario = float(input('Qual o valor do salário? '))
if salario > 1250:
    print('O novo salário com aumento de 10% é de R$ {:.2f}'.format(1.10*salario))
else:
    print('O novo salário com aumento de 15% é de R$ {:.2f}'.format(1.15*salario))
