# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #033
# ---------------------------


n1 = float(input('1º número: '))
n2 = float(input('2º número: '))
n3 = float(input('3º número: '))
if (n1 >= n2) and (n1 >= n3):
    if n2 >= n3:
        print('Maior: {:.2f}\nMenor: {:.2f}'.format(n1, n3))
    else:
        print('Maior: {:.2f}\nMenor: {:.2f}'.format(n1, n2))
elif (n2 >= n1) and (n2 >= n3):
    if n1 >= n3:
        print('Maior: {:.2f}\nMenor: {:.2f}'.format(n2, n3))
    else:
        print('Maior: {:.2f}\nMenor: {:.2f}'.format(n2, n1))
elif (n3 >= n1) and (n3 >= n2):
    if n1 >= n2:
        print('Maior: {:.2f}\nMenor: {:.2f}'.format(n3, n2))
    else:
        print('Maior: {:.2f}\nMenor: {:.2f}'.format(n3, n1))
