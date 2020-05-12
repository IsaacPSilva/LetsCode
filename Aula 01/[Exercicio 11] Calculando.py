'''11. Faça um programa que peça 2 números inteiros e um número real,
calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo.
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.'''

print('VAMOS CALCULAR')
print('-'*40)

num1 = int(input('Informe um valor inteiro: '))
num2 = int(input('Infomre outro valor inteiro: '))
num3 = float(input('Agora informe um valor real: '))

#CALCULANDO (A)
a = num1 * 2 * (num2 / 2)
print('-'*40)
print(f'O valor do produto do primeiro com a metade do segundo é : {a}')

#CALCULANDO (B)
print('-'*40)
b = num1 * 3 + num3
print(f'A soma do triplo do primeiro com o terceiro {b}')

#CALCULANDO (C)
print('-'*40)
c = num3**3
print(f'O terceiro elevado ao cubo {c}')

print('-'*40)
print('FINALIZADO')