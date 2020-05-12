# 7. Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

print('CALCULANDO A ÁREA EM CENTIMETROS DO RAIO DE UM CIRCULO')
print('-'*40)

#Informando raio do circulo
raio = float(input('Informe o raio: '))

print('-'*40)

#Calculando area
area = 3.14 * (raio**2)

#Imprimindo valor
print(f'O valor da area: {area}cm')