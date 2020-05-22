'''6. Faça uma função que recebe uma string e retorna ela ao contrário.
Exemplo: Recebe "teste" e retorna "etset".'''

frase = 'teste'
x = list(frase)
a = x[::-1]

nova_frase = ''.join(a)
print(nova_frase)