"""6. Faça uma função que recebe um número e retorna True se ele é par ou False, se ele é ímpar."""

#Definir função
def test(num):
    valor = num%2==0
    return valor

print(test(21))