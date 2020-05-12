'''9. Faça um programa que peça a temperatura em graus Fahrenheit (F),
transforme e mostre a temperatura em graus Celsius (°C).
°C = (5 * (F-32) / 9)
Obs: Tente também fazer um programa que faça o inverso: peça a
temperatura em graus Celsius e a transforme em graus Fahrenheit.'''

print('CONVERTENDO TEMPERATURA DE (F) PARA (°C)')
print('-'*50)

#Informando valor de Fahrenheit
F = int(input("Valor de Fahrenheit: "))

#CALCULANDO
valor = 5 * (F-32) / 9

#Informando Conversao
print(f'O valor convertido para °C: {valor}')