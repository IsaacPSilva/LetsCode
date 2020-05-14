'''8. Vamos fazer um programa para verificar quem é o assassino de um
crime. Para descobrir o assassino, a polícia faz um pequeno
questionário com 5 perguntas onde a resposta só pode ser sim ou não:
a. Mora perto da vítima?
b. Já trabalhou com a vítima?
c. Telefonou para a vítima?
d. Esteve no local do crime?
e. Devia para a vítima?
Cada resposta sim dá um ponto para o suspeito. A polícia considera
que os suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são
cúmplices e 2 pontos são apenas suspeitos, necessitando outras
investigações. Valores abaixo de 1 são liberados.'''

print("INTERROGATÓRIO")
print('-'*30)

a = input('Mora perto da vítima? ').lower()
b = input('Já trabalhou com a vítima? ').lower()
c = input('Telefonou para a vítima? ').lower()
d = input('Esteve no local do crime? ').lower()
e = input('Devia para a vítima? ').lower()

cont = 0

if a=='sim':
    cont = cont + 1
if b=='sim':
    cont = cont + 1
if c=='sim':
    cont = cont + 1
if d=='sim':
    cont = cont + 1
if e=='sim':
    cont = cont + 1

print(cont)

if cont == 5:
    print('Você é o assassino.')
elif cont == 4 or cont ==3:
    print('Você é um cúmplice')
elif cont == 2:
    print('Você é um suspeito')
else:
    print('Você tá liberado.')
'''
Cada resposta sim dá um ponto para o suspeito. A polícia considera
que os suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são
cúmplices e 2 pontos são apenas suspeitos, necessitando outras
investigações. Valores abaixo de 1 são liberados.'''