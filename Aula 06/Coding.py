#Coding

#Funções
dados = []

def nome_completo():
    informacao_pessoa = []
    nome = input('Informe nome completo: ')
    informacao_pessoa.append(nome)
    idade = int(input('Informe a idade: '))
    informacao_pessoa.append(idade)
    dados.append(informacao_pessoa)

print(dados)

nome_completo()
nome_completo()

print(dados)

