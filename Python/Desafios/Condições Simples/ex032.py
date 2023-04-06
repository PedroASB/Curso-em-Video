# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #032
# ---------------------------


ano = int(input('Digite o ano: '))
if (ano % 400 == 0):
    print('O ano {} é bissexto'.format(ano))
elif (ano % 4 == 0) and (ano % 100 != 0):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

# Maneira alternativa
# ano = int(input('Digite o ano: '))
# if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
#     print('O ano {} é bissexto'.format(ano))
# else:
#     print('O ano {} não é bissexto'.format(ano))
