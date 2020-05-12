#14. Faça um programa que peça um valor monetário e diminua-o em 15%.

print('CALCULANDO VALOR AJUSTADO COM DESCONTO DE 15%')
print('-'*25)


#Recebendo valor
valor = float(input('Informe o valor do produto: R$ '))

#Somando 15%
novo_valor = valor - (valor*15/100)

#Imprimindo
print(f'O novo valor com desconto é R$ {novo_valor}')
print(f'Valor do desconto de 15%: R$ {novo_valor - valor}')