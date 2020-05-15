'''6. Faça um programa, usando loops, que peça para um usuário digitar
um número e que só finaliza quando o usuário digitar 0. Ao final
imprima a soma de todos os números digitados.'''

print("LET'S ADD")
print('-'*20)
#Condicion of exit
print("To exit enter '0'")
print('')

adding = 0

while True:

    #intup of data
    num = int(input('Enter a number: '))
    print(' - '*10)

    #Testing condiccion
    if num == 0:
        print(f'The value of addition is : {adding}.')
        break


    #Incrementing values in additing
    adding = adding + num
    