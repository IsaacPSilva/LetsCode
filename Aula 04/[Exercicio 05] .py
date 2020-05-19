'''5. Faça um programa que imprima o maior número de uma lista, sem
usar o método max().'''

num = [0,1,2,3,4,5,6,7,8,9]
maior = 0
menor = 0

for i in num:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f'O maior é {maior}')
print(f'O menor é {menor}')