'''1. Calcule a soma de até mil termos da série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...
Dica: Use três variáveis:

** um contador, que começa em zero;
** uma variável para a soma de todos os termos, que também começa em zero;
** uma variável para cada termo, que começa em 1 e a cada loop é dividida por 2.

A repetição da soma de mil termos pode ser feita com a função while contador < 1000.'''

i = 0
somatermos = 0


print('SUM')
print('-'*20)

razao = 1

while i<=100:
    razao = (1/2) * razao
    somatermos = somatermos + razao
    i = i + 1
    print(razao, end=' -> ')
print(f'\nThe sum to terms is {somatermos}.')