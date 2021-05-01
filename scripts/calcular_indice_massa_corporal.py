#Calcular (I.M.C)Indice de Massa Corporal.

alt = float(input('Qual sua altura ? '))
peso = float(input('Qual o seu peso ? '))
imc = peso / (alt ** 2)
print('O indice de massa corporal é {:.2f}.'.format(imc))
