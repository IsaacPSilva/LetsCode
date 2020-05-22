'''3. Altere o exercício anterior para que a string copiada alterne entre
letras maiúsculas e minúsculas
Exemplo: se o usuário digitar "latex" o programa deve imprimir
"LaTeX".'''

frase = 'latex'
frase1 = list(frase)

nova_frase = []

for i in range(len(frase1)):
    if i%2==0:
        nova_frase.append(frase1[i].upper())
    if i%2==1:
        nova_frase.append(frase1[i].lower())

frase = ''.join(nova_frase)
print(frase)