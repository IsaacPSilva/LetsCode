#3. Faça um programa que peça um número para o usuário (string), converta-o para float e depois imprima-o na tela. Você consegue fazer a mesma coisa, porém convertendo para int?

#informando número
num = input('Informe um número: ')

print('-'*30)

#Convertendo para float
num_float= float(num)
print(f'O número em número convertido de String para Float é {num_float}')
print(type(num_float))

print('-'*30)

#Convertendo de float para inteiro
num_int = int(num_float)
print(f'O número convertido de Float para Inteiro é {num_int}')
print(type(num_int))