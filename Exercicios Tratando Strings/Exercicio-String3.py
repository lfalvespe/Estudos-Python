""" Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO".  """

cidade = str(input('Digite o nome de uma cidade: ')).upper().strip()

lista = cidade.split()

print('A cidade digitada começa com Santo?')
print(lista[0] == 'SANTO')