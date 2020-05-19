'''4. Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.'''

numbers = [0,1,2,3,4,5,6,7,8,9]

for num in numbers:
    if num%2 == 0:
        print(f'The number {num} is pair')