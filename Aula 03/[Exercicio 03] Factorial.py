'''3. Peça ao usuário para digitar um número e imprima o fatorial de n.'''

number = int(input('Enter a number: '))
mul = fac = number

while fac != 0:
    print(fac, end=' ')
    fac = fac - 1
    mul = fac * (fac -1)