'''9. Um produto vai sofrer aumento de acordo com a Tabela 1 abaixo. Faça um programa que peça para o usuário digitar o valor do produto de acordo com o preço antigo e escreva uma das mensagens da Tabela 2, de acordo com o preço reajustado:

Preço Antigo Percentual de aumento
|Até R$ 50 5% | Entre R$ 50 e R$100 10% | Entre R$100 e R$150 13% | Acima de R$150 15%

Preço Novo Mensagem
Até R$80 Barato
Entre R$ 80 e R$115 Razoável
Entre R$ 115 e R$150 Normal
Entre R$ 150 e R$170 Caro
Acima de R$170 Muito caro'''

print('{:^30}'.format('MARKET'))
print('-'*30)

#receiving price for adjust
value = float(input('What is the value of product: '))

if value <=50 and value>0:
    newValue = value * 1.05
elif value>50 and value <=100:
    newValue = value * 1.10
elif value>100 and value<=150:
    newValue = value * 1.13
elif value>150:
    newValue = value * 1.15
elif value <=0:
    print('Invalid value')

if newValue <=80 and newValue>0:
    print(f'The new value is $ {newValue:.2f}. The product value is cheap.')
elif newValue>80 and newValue<=115:
    print(f'The new value is $ {newValue:.2f}. The product value is reasonable.')
elif newValue>115 and newValue<=150:
    print(f'The new value is $ {newValue:.2f}. The product value is normal.')
elif newValue>150 and newValue<=170:
    print(f'The new value is $ {newValue:.2f}. The product value is expensive.')
elif newValue>170:
    print(f'The new value is $ {newValue:.2f}. The product value is very expensive.')