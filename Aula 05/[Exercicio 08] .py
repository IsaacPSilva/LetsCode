'''8. Faça uma função que receba um texto e uma palavra, então verifique
se a palavra está no texto, retornando True ou False.'''

#Receber palavra para verificar
texto = 'Python é muito legal'.lower()
palavra = input('Informe a palavra para verificar: ')

if palavra in texto:
    print('Verificando: ', palavra in texto)
    print(f'A palavra contém no texto.')
else:
    print('Verificando: ', palavra in texto)
    print(f'A palavra não contém no texto.')

print("TEXTO: 'Python é muito legal'")