'''5. Faça um programa que leia a validade das informações:
a. Idade: entre 0 e 150;
b. Salário: maior que 0;
c. Sexo: M, F ou Outro;
O programa deve imprimir uma mensagem de erro para cada
informação inválida.'''

print('TESTING INFORMATION')
print('-'*30)

#Input of data
age = int(input('Insert the age: '))
if age>=0 and age<=150:
    print('Valid age')
    print('-'*30)
else:
    print('Invalid value')
    print('-'*30)

salary = float(input('Insert the salary: R$ '))
if salary>0:
    print('Valid salary')
    print('-'*30)
else:
    print('Invalid value')
    print('-'*30)

sex = input('Insert the sex [M,F, Others] : ').lower()
if sex=='m' or sex=='f' or sex=='others':
    print('Valid sex')
    print('-'*30)
else:
    print('Invalid value')
    print('-'*30)
