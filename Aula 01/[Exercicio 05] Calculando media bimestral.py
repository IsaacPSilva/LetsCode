#5. Faça um programa que peça as 4 notas bimestrais de um aluno e mostre a média aritmética delas.

print('CALCULANDO MÉDIA ANUAL')

print('-'*30)

#Recebendo a entrada das notas
nota1 = float(input('Informe a 1º nota: '))
nota2 = float(input('Informe a 2º nota: '))
nota3 = float(input('Informe a 3º nota: '))
nota4 = float(input('Informe a 4º nota: '))

#Realizando calculo da divisao das notas
soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

print('-'*30)

#Imprimindo media
print(f'A media anual do aluno foi {media}')