'''Crie um programa que gere 5 números aleatórios e coloque numa Tupla. Mostre:

a)A listagem
b) o maior e o menor valor da Tupla.

'''
from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10) )

print('Os números sorteados foram: ', end = '')
for c in num:
  print(f'{c}', end = " ")


print(f'\nO menor valor é {min(num)}')
print(f'O maior valor é {max(num)}')