'''Faça um programa que peça a idade do usuário e imprima se ele é
maior ou menor de 18 anos.'''

#Informando entrada de dados

print('VERIFICADOR DE MAIORES DE IDADE')
print('-'*30)

#Recebendo entrada de dados idade
idade = int(input('Informe a idade: '))

if idade>=18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')