#13. Faça um programa que peça um valor monetário e aumente-o em 15%. Seu programa deve imprimir a mensagem “O novo valor é R$[valor]”.

print('CALCULANDO VALOR AJUSTADO COM ACRESCIMO DE 15%')
print('-'*25)


#Recebendo valor
valor = float(input('Informe o valor do produto: R$ '))

#Somando 15%
novo_valor = valor + (valor*15/100)

#Imprimindo
print(f'O novo valor é R$ {novo_valor}')
print(f'Valor adicionado dos 15%: R$ {novo_valor - valor}')