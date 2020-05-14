'''3. Faça um programa que dado um número digitado, mostre se ele é
Par ou Ímpar.'''

print("Let's Go checkin if the number is pair ou odd.")
print('-'*50)

#Receiving number in input
num = int(input('Enter the number: '))
print('-'*50)

#Checking the number
if num%2 == 0:
    print(f'The number {num} is even.')
else:
    print(f'The number {num} is odd.')