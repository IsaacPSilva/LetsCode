'''9. Faça um programa que pede para o usuário digitar 5 números e, ao final, imprime uma lista com os 5 números digitados pelo usuário (sem converter os números para int ou float).
Exemplo: Se o usuário digitar 1, 5, 2, 3, 6, o programa deve imprimir a lista ['1','5','2','3','6']'''

lists = []
i = 0

print('Adding values in lists')
print('-'*30)
print('')

#Information values of input
while i < 5:
    num = input('Enter a number: ')
    lists.append(num)
    i += 1

#Printing values information
print(lists)