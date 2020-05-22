'''7. Faça uma função que sorteia 10 números aleatórios entre 0 e 100 e retorna o maior entre eles.'''
import random

def sorteio():
    maior = 0
    menor = 0
    for i in range(10):
        x = random.randint(0,100)
        if i==1:
            menor = x
            
        if x<menor:
            menor = x
        if x>maior:
            maior = x

    print('Menor: ', menor)
    print('Maior: ', maior)

sorteio()