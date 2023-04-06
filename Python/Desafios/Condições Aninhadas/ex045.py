# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #045
# ---------------------------


from random import randint
from time import sleep
print('\033[34m-=-\033[m'*15)
print('{}{} JOKENPÔ {}{}'.format('\033[1;34m', '=='*9, '=='*9, '\033[m'))
print('\033[34m-=-\033[m'*15)
comp = randint(1, 3)
print('\033[33mPEDRA = 1 | PAPEL = 2 | TESOURA = 3\033[m')
user = int(input('\033[35mFAÇA SUA ESCOLHA: \033[m'))
print('\033[3;34mPROCESSANDO... \033[m')
sleep(1.5)
if comp == 1:
    if user == 1:
        print('\033[36mEMPATOU!\033[m')
    elif user == 2:
        print('\033[32mVOCÊ VENCEU!\033[m')
    elif user == 3:
        print('\033[31mVOCÊ PERDEU!\033[m')
    else:
        print('\033[1mESCOLHA INVÁLIDA!\033[m')
elif comp == 2:
    if user == 1:
        print('\033[31mVOCÊ PERDEU!\033[m')
    elif user == 2:
        print('\033[36mEMPATOU!\033[m')
    elif user == 3:
        print('\033[32mVOCÊ VENCEU!\033[m')
    else:
        print('\033[1mESCOLHA INVÁLIDA!\033[m')
elif comp == 3:
    if user == 1:
        print('\033[32mVOCÊ VENCEU!\033[m')
    elif user == 2:
        print('\033[31mVOCÊ PERDEU!\033[m')
    elif user == 3:
        print('\033[36mEMPATOU!\033[m')
    else:
        print('\033[1mESCOLHA INVÁLIDA!\033[m')
