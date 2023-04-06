# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #031
# ---------------------------


d = int(input('Qual a distância da viagem em km? '))
if d < 200:
    print('O preço da passagem é R$ {}'.format(0.50*d))
else:
    print('O preço da passagem é R$ {}'.format(0.45*d))
