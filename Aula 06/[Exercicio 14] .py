"""14. Faça uma função que recebe uma lista de números e retorna a média aritmética dos elementos dessa lista. Desafio"""

#information funcion
def fun(list_one, list_two):
    tot = 0
    notes_fist = 0
    notes_second = 0
    for i in list_one:
        notes_fist += i
    for i in list_two:
        notes_second += i
    s = len(list_one) + len(list_two)
    tot = float(notes_fist+notes_second)/s
    return tot

#Lists of input
lista1 = [10,6,4,8.4,4.4,2,6.6,4.1]
lista2 = [2,5,2.3,4,5,7,7,4,10,10]

#funcions declaration
x = fun(lista1,lista2)
#printing values return
print(f'The average is: {x:.2f}')