'''8. Faça um programa que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas digitadas sejam válidas.
a. Idade: entre 0 e 150;
b. Salário: maior que 0;
c. Sexo: M, F ou Outro.'''

print('RECORDING INFORMATION')
print(' - '*10)

while True:
    age = int(input('Enter the age [0 to 150]: '))
    while age<0 or age>150:
        age = int(input('Invalid value. Enter the age [0 to 150]: '))

    salary = float(input('Enter the value of salary [>0]: $ '))
    while salary<0:
        salary = float(input('Invalid value. Enter the value of salary [>0]: $ '))

    gender = input('Enter the gender [M,F, others] :  ').lower()
    while gender !='f' and gender!='others' and gender !='m':
        gender = input('Invalid value. Enter the gender [M,F, others] :  ').lower()