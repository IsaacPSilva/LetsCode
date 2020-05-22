"""9. Faça uma função que recebe uma lista de palavras e retorna uma lista contendo as mesmas palavras da lista anterior, porém escritas em caixa alta."""

#Função
def fun(transforme):
    nova_lista = []
    for x in transforme:
        nova_lista.append(x.upper())
    print(nova_lista)

#Lista de palavra para transformar em caixa alta
palavras = ['maria', 'joao', 'pedro', 'adanias']

#Chama a função para trabalhar
fun(palavras)