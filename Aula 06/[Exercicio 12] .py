"""12. Faça uma função que recebe um número x e uma lista numérica e
retorna uma lista cujos elementos são os itens da lista de entrada
multiplicado por x.
Exemplo: se a função receber o número 5 e a lista [3,5,1], então a
função deve retornar [5x3, 5x5, 5x1] = [15, 25, 5]."""


#definir função
def fun(number, list):
    tot = []
    for i in list:
        tot.append(num * i)

    return tot

lista = [9,8,7,6,5,4,3,2,1]#Informando valores da função em uma variavel
num = int(input('Enter a number: '))
x = fun(num, lista)
print(x)