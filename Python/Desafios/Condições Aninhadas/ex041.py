# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #041
# ---------------------------


from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nasc
if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JÚNIOR')
elif idade == 20:
    print('SÊNIOR')
elif idade > 20:
    print('MASTER')
else:
    print('Idade inválida')
