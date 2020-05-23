"""10. Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.
Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a
função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4]."""

#definir função
def fun(list1, list2):
    soma = []
    if len(list1)==len(list2):
        for i in range(len(list1)):
            soma.append(list1[i] + list2[i])
    print(soma)


lista1 = [1,2,3]
lista2 = [4,5,6]

fun(lista1, lista2)