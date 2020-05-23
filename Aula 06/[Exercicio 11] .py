"""11. Faça uma função que receba duas listas e retorne o produto item a
item dessas listas.
Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a
função deve retornar [1x3, 4x5, 3x1] = [3, 20, 3]."""

#definir função
def fun(list_one, list_two):
    res = []
    if len(list_one)==len(list_two):
        for i in range(len(list_one)):
            res.append(list_one[i]*list_two[i])
    else:
        res = 'Listas são diferentes tamanhos'
    return res
    

lista1 = [1,4,3]
lista2 = [3,5,11]
x = fun(lista1,lista2)
print(x)