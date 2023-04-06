# ---------------------------
# Curso em Vídeo - Python
# Autor: github.com/PedroASB
# ---------------------------
#       Exercício #043
# ---------------------------


altura = float(input('Digite sua altura (m): '))
peso = float(input('Digite seu peso: (kg): '))
imc = peso / altura**2
if imc < 18.5:
    print('IMC: {:.1f} | Abaixo do peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('IMC: {:.1f} | Peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('IMC: {:.1f} | Sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('IMC: {:.1f} | Obesidade'.format(imc))
else:
    print('IMC: {:.1f} | Obesidade mórbida'.format(imc))
