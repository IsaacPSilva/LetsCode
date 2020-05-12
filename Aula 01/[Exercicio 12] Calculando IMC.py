"""12. Faça um programa que peça o peso e altura de uma pessoa e calcule
seu IMC (Índice de Massa Corporal).
Obs: IMC = Peso/Altura2"""

print(f'CALCULANDO I.M.C')
print(f'-'*20)

#Informando valores de entrada
altura = float(input('Informe a altura: '))
peso = float(input('Informe o peso: '))

#Calculando dados
imc = peso / (altura*altura)
print('-'*20)

print(f'O valor do I.M.C é: {imc:.2f}')