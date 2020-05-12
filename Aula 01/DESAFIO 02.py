#2. Faça um programa que informe a data e a hora para o usuário. Para isso use a função datetime.now() do módulo datetime.

#Importando biblioteca datetime
from datetime import datetime

#Atribuindo funcao para uma variavel
hora_e_data_atual = datetime.now()

#Imprimindo dados
print('INFORMAÇÕES EM TEMPO REAL')
print('-'*30)
print(hora_e_data_atual)
print('-'*30)