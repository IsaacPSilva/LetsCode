'''8. Faça um programa que dadas duas listas de mesmo tamanho, imprima o produto escalar entre elas.
OBS: produto escalar é a soma do resultado da multiplicação entre o número na posição i da lista1 pelo número na posição i da lista2, com i variando de 0 ao tamanho da lista.'''

lista1 = [1, 4, 5]
lista2 = [2, 2, 3]
lista3 = []
soma = 0

for i in range(len(lista1)):
    l3 = lista1[i] * lista2[i]
    lista3.append(l3)

for i in range(len(lista3)):
    soma = soma + lista3[i]

print(f'Segue os valores da lista 03 = {lista3}. A soma total é :', end=' ')
print(soma)