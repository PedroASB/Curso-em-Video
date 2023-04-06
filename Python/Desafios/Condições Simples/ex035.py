# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #035
# ---------------------------


a = int(input('Reta 1: '))
b = int(input('Reta 2: '))
c = int(input('Reta 3: '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('É possivel formar um triângulo com os lados {}, {} e {}'.format(a, b, c))
else:
    print('Não é possível formar um triângulo com os lados {}, {} e {}'.format(a, b, c))
