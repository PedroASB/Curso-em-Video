# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #028
# ---------------------------


from random import randint
comp = randint(0, 5)
user = int(input('Escolhi um número entre 0 e 5, adivinhe qual é: '))
if user == comp:
    print('Venceu, parabéns!')
else:
    print('Perdeu, que pena!')
