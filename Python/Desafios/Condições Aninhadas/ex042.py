# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #042
# ---------------------------


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
