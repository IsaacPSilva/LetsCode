'''3. Faça uma função para cada operação matemática básica (soma,
subtração, multiplicação e divisão). As funções devem receber dois
números e retornar o resultado da operação.'''

#Definir função
def soma(v1, v2):
    return v1 + v2

def subtração(v1, v2):
    return v1 - v2

def multiplicação(v1, v2):
    return v1 * v2

def divisao(v1, v2):
    return v1 / v2


v1 = 120
v2 = 6

print(f'A soma entre {v1} + {v2} = ',soma(v1, v2))

print(f'A subtração entre {v1} - {v2} = ',subtração(v1, v2))

print(f'A multiplicação entre {v1} x {v2} = ',multiplicação(v1, v2))

print(f'A divisão entre {v1} / {v2} = ',divisao(v1, v2))

