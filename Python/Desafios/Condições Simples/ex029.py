# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #029
# ---------------------------


v = int(input('Qual a velocidade? '))
if v > 80:
    print('Você ultrapassou 80 km/h e foi multado em R$ {:.2f}'.format(7*(v-80)))
