'''9. Faça uma função que receba uma string que contém tanto números
quanto letras e caracteres especiais, e que separe as letras em uma
variável e os números em outra (os caracteres especiais podem ser
descartados). Ao final a função deve imprimir as duas variáveis.'''

texto = 'O numero PI é 3.14'

lista_palavras = []
lista_numeros = []

for i in texto:
    if i.isalpha()==True:
        lista_palavras.append(i)
    if i.isnumeric()==True:
        lista_numeros.append(i)

print(f'Letras: {lista_palavras}.')
print(f'Letras: {lista_numeros}.')