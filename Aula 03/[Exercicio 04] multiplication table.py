'''4. Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.'''

print('multiplication table'.upper())
print('-'*30)

#Information values of variables
value = 9
number = 1

#Checking condition
while number<10:
    print(value, ' X ', number, ' = ', value*number)
    #Incrementing one more for each repetition
    number += 1
print('-'*30)
print('Finished.')