#8. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês e depois, calcule e mostre o total do seu salário no referido mês.

print('CALCULANDO SALÁRIO COM BASE NAS HORAS TRABALHO')
print('-'*50)

#Informando valor das horas e quanto tempo de trabalho no mês
valor = float(input('Qual o valor por hora? '))
horas = int(input('Quantas horas foram trabalhadas no mês? '))

print('-'*50)

#Calculando salário
salario = valor * float(horas)

#Informando salario
print(f'O salario do mês com base nas horas e no valor é R$ {int(salario)}')