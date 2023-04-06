# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #037
# ---------------------------


dec = int(input('Digite um número em decimal: '))
print('Para qual base deseja fazer a conversão? ')
opt = int(input('1: Binário\n2: Octal\n3: Hexadecimal\n'))
if opt == 1:
    print('{} Em binário é \033[34m{}\033[m'.format(dec, bin(dec)))
elif opt == 2:
    print('{} Em octal é \033[34m{}\033[m'.format(dec, oct(dec)))
elif opt == 3:
    print('{} Em hexadecimal é \033[34m{}\033[m'.format(dec, hex(dec)))
else:
    print('{}Opção inválida!{}'.format('\033[31m', '\033[m'))
