'''10. Pegue a lista gerada no exercício anterior e transforme cada um dos itens dessa lista em um float.
OBS: Não é para alterar o programa anterior, mas sim a lista gerada por ele.'''

lists = []
i = 0

print('Adding values in lists')
print('-'*30)
print('')

#Information values of input---Attetion: The value information is a STRING
while i < 5:
    num = input('Enter a number: ')
    lists.append(num)
    i += 1

#Printing values information
print(f'The old list is : {lists)


new_list = []
#Converting values of a lists in FLOAT.
for i in lists:
    new_number = float(i)
    new_list.append(new_number)
print(f'The new list is : {new_list}')