'''7. Faça um programa que sorteia um número N e peça para o usuário
adivinhar o número sorteado. A cada resposta errada, o seu programa
deve imprimir um aviso dizendo que a resposta está errada e pedir
novamente uma resposta ao usuário.'''

#Importing library random
import random

print('Try guess the number of 0 ot 10.')
print("For exit enter '00'")
print('')

while True:
    #Random 
    value = random.randint(0,10)

    #Informing number
    num = int(input('Enter a number: '))

    #Checking condition of exit
    if num==00:
        break

    #Testing condition 
    if num==value:
        print('You Win\n')
    else:
        print(f'You Less - The number is {value}\n')
