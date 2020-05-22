'''8. Faça uma função que recebe um número n de entrada, sorteia n números aleatórios entre 0 e 100 e retorna a média deles.'''
import random


#Definir função
def fun(n):
    #Acumular soma de numeros
    soma = 0

    #Sorteando numeros
    for i in range(n):
        x = random.randint(0,100)
        soma += x

    #Calcular media
    media = soma / n

    print(f'O total é : {soma}')
    print(f'A média é : {media}')


num = int(input('Enter a number: '))
fun(num)