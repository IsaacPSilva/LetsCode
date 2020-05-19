'''6. Agora usando o método max() faça um programa que imprima os três maiores números de uma lista.
Dica: Use o método próprio de listas .remove().'''

num = [50,60,77,4,55,10]
num2 = []
i = 0

while i < 3:
    maior = max(num)
    num2.append(maior)
    num.remove(maior)
    i =+ 1
print(num2)