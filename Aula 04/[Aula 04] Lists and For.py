### LISTAS ###
'''
numero1 = 1
numero2 = 2

listinha = []
print(listinha)



# indices:    0       1           2       3   
numeros = [numero1, numero2, 'palavra', 2>1]
print(type(numero1))


#print(numeros[0], numeros[1], numeros[2], numeros[3], numeros[4])

numeros[1] = 1000
numeros[2] = 'textotextotextotexto'

#print(numeros[0], numeros[1], numeros[2], numeros[3], numeros[4])


i = 0

##        length ou tamanho da lista
while i < len(numeros):

    print(numeros[i])

    i = i + 1
    # i += 1 faz a mesma coisa

# IndexError: list index out of range => os índices acabaram!
# Você ta tentando acessar um indice que nao existe!
'''

'''
animais = ['andorinha', 'boto', 'dromedario', 'cao']

resposta = input('Você quer acrescentar animais à lista? (s/n) ')

while resposta == 's':
    elemento_novo = input('Digite um novo animal: ')

    # append acrescenta um elemento (dentro do parenteses) à lista
    animais.append(elemento_novo)


    resposta = input('Você quer acrescentar animais à lista? (s/n) ')


# remove para remover um elemento
#animais.remove('suricato')

# pop para remover um elemento com base no indice
#animais.pop(2)

# count para contar um elemento com determinado valor
numero_suricatos = animais.count('suricato')

print(animais)

print(numero_suricatos)

print('O numero de animais é: ', len(animais))

animais.sort(reverse=True)

print(animais)
'''

lista_numeros = [412,5123,6412,51,356,3,631,613,613,1356,613,1]


# comando(lista)
print(min(lista_numeros), max(lista_numeros), len(lista_numeros))

# variavel = lista.count('elemento')




### FOR ###


'''
i=0
while i < len(fib):
    print(fib[i])
    i = i + 1
'''

# elemento não precisa ser definida!!!
'''
for elemento in fib:
    print(elemento*2)
    elemento_novo = elemento - 1000
    print(elemento_novo)

print(fib)
print(elemento)

floresta = ['árvore', 'lago', 'folha', 'capivara']

for qualquercoisa in floresta:
    print(qualquercoisa)
'''

'''
# ind  0  1  2  3  4  5  6
fib = [1, 1, 2, 3, 5, 8, 13]


#indices= [0,1,2,3,4,5,6,7,8,9,10]
indices = range(11)
print(indices)

for i in range(len(fib)):
    fib[i] = 10 + i*10


print(fib)
'''


animais = []

resposta = input('Você quer acrescentar animais à lista? (s/n) ')

while resposta == 's':

    elemento_novo = input('Digite um novo animal: ')

    # append acrescenta um elemento (dentro do parenteses) à lista
    animais.append(elemento_novo)

    resposta = input('Você quer acrescentar animais à lista? (s/n) ')



animais_2 = ['suricato', 'cachorro', 'cobra', 'garça', 'papagaio']

'''
for elemento in animais:
    nova_lista.append(elemento)
'''
'''
for elemento in animais:
    for elemento2 in animais_2:
        print(elemento, elemento2)
        if elemento == elemento2:
            print('Esses elementos são iguais')
'''

# i percorre range(5)=[0,1,2,3,4]
for i in range(len(animais)):
    # print está printando animais[0] e animais_2[0]
    # print está printando animais[1] e animais_2[1]
    # print está printando animais[2] e animais_2[2]

    print(animais[i], animais_2[i])

    # a comparação é feita entre animais[0] e animais_2[0]
    # a comparação é feita entre animais[1] e animais_2[1]
    # a comparação é feita entre animais[2] e animais_2[2]
    if animais[i] == animais_2[i]:
        print('Esses elementos são iguais')



for elemento in animais:
    for elemento2 in animais_2:
        print(elemento, elemento2)
        if elemento == elemento2:
            print('Esses elementos são iguais')


