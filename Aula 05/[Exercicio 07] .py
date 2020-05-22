'''7. Agora faça uma função que recebe uma palavra e diz se ela é um
palíndromo, ou seja, se ela é igual a ela mesma ao contrário.
Dica: Use a função do exercício 5.'''

#Verificando se a palavra é um palindromo

#Receber palavra para verificar
palavra = input('Informe uma palavra: ').lower()


analise = palavra
x = list(analise)
a = x[::-1]

nova_frase = ''.join(a)

if palavra==nova_frase:
    print('É um palíndromo')
elif palavra!=nova_frase:
    print('Não é palíndromo:')