# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #040
# ---------------------------


n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2
if m >= 7:
    print('Média: {:.2f} | {}APROVADO!{}'.format(m, '\033[32m', '\033[m'))
elif m < 5:
    print('Média: {:.2f} | {}REPROVADO!{}'.format(m, '\033[31m', '\033[m'))
else: # m >= 5 and m < 7
    print('Média: {:.2f} | {}RECUPERAÇÃO!{}'.format(m, '\033[33m', '\033[m'))
