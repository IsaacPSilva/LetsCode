'''7. Faça um programa que mostre uma questão de múltipla escolha com
5 opções (letras a, b, c, d, e e). Sabendo a resposta certa, o programa
deve receber a opção do usuário e informar a letra que o usuário
marcou e se a resposta está certa ou errada.'''

print('Multiple choice question.')
print('-'*30)

#Question of proof
print("What's the linguage used in the course ?")
print('a) PHP')
print('b) HTML')
print('c) PYTHON')
print('d) JAVA')
print('e) C++')

#receiving input of question data.
print('-'*30)
question = input('Inform the correct question: ').lower()
print('-'*30)

if question=='c':
    print('Correct opction.')
elif question=='a' or question=='b' or question=='d' or question=='e':
    print('Wrong option.')
else:
    print('Invalid option')