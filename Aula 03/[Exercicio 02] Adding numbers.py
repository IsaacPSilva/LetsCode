#2. Peça ao usuário para digitar um número n e some todos os números de 1 a n.

print("LET'S ADD")
print('-'*20)

#Information number for score
value = int(input('Enter a number: '))
print('-'*20)

#Insert counter for repetion
cont = 1
soma = 0

#
while soma <= value:
    soma = soma + cont
    cont = cont + 1
    print(soma, end=' ')
print(' -> FINISH')