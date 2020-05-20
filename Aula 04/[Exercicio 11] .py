'''11. Faça um Programa que peça as 4 notas bimestrais e mostre a média aritmética delas, usando listas.'''

print("LET'S SUM MEAN OF NOTES")
#Checking mean of notes

#Insert values in list
nota = []
i=0

#Come in condition
while i < 4:
    value = float(input(f'Enter a {i+1}ª note: '))
    nota.append(value)
    i += 1

#Realize mean of list sum
mean = sum(nota)/len(nota)
print(mean)