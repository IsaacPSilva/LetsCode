'''6. Escreva um programa que peça a nota de 3 provas de um aluno e
verifique se ele passou o não de ano.
Obs.: O aluno irá passar de ano se sua média for maior que 6.'''

print('{:^30}'.format('High School'))
print('-'*30)

#Inserting notes
note1 = float(input('Insert the first note: '))
note2 = float(input('Insert the second note: '))
note3 = float(input('Insert the third note: '))
print('-'*30)

#Calculat average of notes
average = (note1 + note2 + note3) / 3

if average>=6:
    text = 'Approved student.'
else:
    text = 'Recovery student.'

#show avegare of notes.
print(f'The average of notes is {average:.2f}. {text}')