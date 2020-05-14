### Malha de repetição (loop) - While

'''
O while é bastante parecido com um 'if': ele possui uma expressão,
e é executado caso ela seja verdadeira.

Mas o if é executado apenas uma vez e depois o código segue adiante.
O while não: ao final de sua execução, ele torna a testar a expressão,
e caso ela seja verdadeira, ele repete sua execução.
'''

'''
Uma utilidade interessante do while é obrigar o usuário a
digitar apenas entradas válidas.
'''

# o exemplo abaixo não aceita um salário menor do que o mínimo atual:
salario = 0.0
while salario < 998.0:
    salario = float(input('Digite o seu salário: '))
print('Você ganha ', salario)

'''
Todo tipo de código que deve se repetir várias vezes pode ser feito
com o while, como somar vários valores, gerar uma sequência etc.
Nestes casos, é normal utilizar um contador:
'''
numero = int(input('Digite quantas provas você fez: '))
contador = 1
soma = 0
while contador <= numero:
    nota = float(input('Digite a nota da prova ' + str(contador) + ':'))
    soma = soma + nota
    contador = contador + 1
media = soma/numero
print('Você fechou com média:', media)

'''
Um jeito de forçar um loop a ser interrompido é utilizando o comando 'break'.
O loop abaixo em tese seria infinito, mas se a condição do if for verificada,
o break é executado e conseguimos escapar do loop:
'''
while True:
    resposta = input('Digite SAIR para sair: ')
    if resposta == 'SAIR':
        break
    else:
        print('E lá vamos nós de novo...')
