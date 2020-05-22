'''1. Faça uma função que receba uma string e uma letra e:
a. imprima quantas vezes a letra aparece na string;
b. imprima todas as posições em que a letra aparece na string;
c. retorne a distância entre a primeira e a última aparição dessa letra na string.'''

#Texto para analisar
texto = 'Na matemática, o número é uma proporção numérica definida pela relação entre o perímetro de uma circunferência e seu diâmetro; por outras palavras, se uma circunferência tem perímetro e diâmetro, então aquele número é igual a.'.lower()

#Criando lista com as palavras
x = texto.split()

#Informando a palavra para analisar dentro do texto
palavra = 'número'

#print(x)

# [r:a] definir contador para numero de vezes
cont = 0

# [r:b] criando lista para marcar posição
pos = []


#Inicializar verificação
for i in range(len(x)):
    if x[i]==palavra:
        pos.append(i)
        cont += 1

# [a] Informando numero de vezes
print(f"O número de vezes que a palavra '{palavra}' foi encontrada no texto: {cont:02d}x.")


# [b] imprima todas as posições em que a letra aparece na string;
print(f"A palavra'{palavra}' foi encontrada no texto na posição: {pos}.")



# [c] retorne a distância entre a primeira e a última aparição dessa letra na string.
if len(pos)>1:
    print(f'A distancia entre a primeira palavra e ultima palavra encontrada é: {pos[cont-1] - pos[0]}.')
else:
    print(f'So Foi encontrando uma palavra de "{palavra}" no texto.')
