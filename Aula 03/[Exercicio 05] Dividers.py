'''5. Faça um programa que recebe um número inteiro do usuário e imprime na tela a quantidade de divisores desse número e quais são eles.'''

print('CHECKING A NUMBER DIVIDERS')
print('-'*40)


#Receiving input of data.
number = int(input('Enter a number: '))

while number!=0:
    if number%2==0:
        print(number, end=' | ')
        number = number/2
    elif number%3==0:
        print(number, end=' | ')
        number = number/3
    elif number%5==0:
        print(number, end=' | ')
        number = number/5
    elif number%7==0:
        print(number, end=' | ')
        number = number/7
    elif number%11==0:
        print(number, end=' | ')
        number = number/11