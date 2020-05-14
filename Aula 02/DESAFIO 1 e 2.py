'''1. Faça um programa que leia 3 números e informe o maior deles.'''

'''num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num3 = int(input('Digite o 3° número: '))

if num1>=num2 and num1>=num3:
    print(f'O número maior é {num1}')
elif num2>=num1 and num2>=num3:
    print(f'O número maior é {num2}')
elif num3>=num1 and num3>=num2:
    print(f'O número maior é {num3}')'''



num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num3 = int(input('Digite o 3° número: '))
num4 = int(input('Digite o 4° número: '))

if num1>=num2 and num1>=num3 and num1>=num4:
    print(f'O número maior é {num1}')
elif num2>=num1 and num2>=num3 and num2>=num4:
    print(f'O número maior é {num2}')
elif num3>=num1 and num3>=num2 and num3>= num4:
    print(f'O número maior é {num3}')
elif num4>=num1 and num4>=num2 and num4>=num3:
    print(f'O número maior é {num4}')