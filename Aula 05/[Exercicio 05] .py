"""5. Faça uma função que receba uma string e retorne uma nova string
substituindo:
'a' por '4'
'e' por '3'
'I' por '1'
't' por '7'"""

a = input('Informe uma frase: ')
x = a.replace('a', '4').replace('e', '3').replace('I', '1').replace('t', '7')

print(x)