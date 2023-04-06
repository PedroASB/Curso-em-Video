# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #044
# ---------------------------


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
