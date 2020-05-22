"""2. Super Desafio! - faça uma função que criptografa uma mensagem
substituindo cada letra pela letra oposta do dicionário:
'a' por 'z'
'b' por 'y'
'c' por 'x'"""

texto = 'Na matemática, o número é uma proporção numérica definida pela relação entre o perímetro de uma circunferência e seu diâmetro; por outras palavras, se uma circunferência tem perímetro e diâmetro, então aquele número é igual a.'.lower()

text2 = texto.replace('a', 'z').replace('b', 'y').replace('c', 'x')
print(text2)

"""
import string
def criptografa(mensagem):
    alfabeto1 = string.ascii_lowercase #retorna uma string com todas as letras do alfabeto minúsculas = abcdefghijklmnopqrstuvwxyz
    alfabeto2 = string.ascii_uppercase #retorna uma string com todas as letras do alfabeto maiúsculas = ABCDEFGHIJKLMNOPQRSTUVWXYZ
    nova_mensagem = ""
    for item in mensagem:
        if item in alfabeto1:
            indice = alfabeto1.index(item)
            letra_oposta = alfabeto1[-1 - indice]
            nova_mensagem += letra_oposta
        elif item in alfabeto2:
            indice = alfabeto2.index(item)
            letra_oposta = alfabeto2[-1 - indice]
            nova_mensagem += letra_oposta
        else:
            nova_mensagem += item
    return nova_mensagem

texto = "aBcd eFghij kLmn"
criptografado = criptografa(texto)
print(criptografado)
print(criptografa(criptografado)) # Texto original

"""