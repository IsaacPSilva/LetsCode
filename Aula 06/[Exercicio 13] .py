"""13. Faça uma função que recebe uma lista de números e retorna a soma
dos elementos dessa lista.
"""

#information funcion
def fun(list_one, list_two):
    tot = 0
    for i in list_one:
        tot += i
    for i in list_two:
        tot += i
    return tot

#Lists of input
lista1 = [10,6,4,84,44,2,66,41]
lista2 = [2,5,23,45,77,4,100]

#funcions declaration
x = fun(lista1,lista2)
#printing values return
print(x)