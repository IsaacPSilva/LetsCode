'''1. Faça um programa que peça ao usuário um número e imprima todos os números de um até o número dado.
Exemplo: digite: 5, imprime: 1 2 3 4 5'''

print("{:^30}".format("LET'S GO"))
print('-'*30)

#Data input
num = int(input('Insert the number: '))
valor = 1

#Testing codicion for enter
while valor <= num:
    print(valor, end=' ')
    #Incrementing value in variable
    valor = valor + 1

print('\nFINISED!')