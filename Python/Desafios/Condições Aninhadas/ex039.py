# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #039
# ---------------------------


from datetime import date
ano_nasc = int(input('Você nasceu em que ano? '))
idade = date.today().year - ano_nasc
if idade < 18:
    print('\033[1mVocê ainda vai ser dispensado!\033[m Falta {} ano(s)!\n'.format(18-idade))
elif idade == 18:
    print('\033[1mHora de ser dispensado!\033[m\n')
else:
    print('\033[1mJá foi dispensado!\033[m Passou {} ano(s)\n'.format(idade-18))
print('\033[4;33mAlistamento obrigatório é um absurdo!\033[m')
print('\033[1;31mPelo fim das práticas obsoletas do Exército brasileiro!\033[m')
