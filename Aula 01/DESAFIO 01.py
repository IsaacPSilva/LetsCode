'''1. Peça para o usuário digitar uma velocidade inicial (em m/s), uma
posição inicial (em m) e um instante de tempo (em s) e imprima a
posição de um projétil nesse instante de tempo.'''

print('DESAFIO 01 - FISICA')
print('-'*30)

#Informando valores
vel_ini = int(input('Qual a velocidade em m/s?  '))
pos_ini = int(input('Qual a posição inicial em metros ?  '))
ins_tem = int(input('Qual o instante de tempo ?  '))

print('-'*30)

#Definindo valores
g = -10 #m/s
v0 = vel_ini
y0 = pos_ini
t = ins_tem
'''pos_projetil = yt'''

#Efetuando operação
yt = y0 + v0 * t + ((g*t**2)/2)

#Imprimindo resultado da operação
print(f'A Posição final do projetil é {yt:.0f}')