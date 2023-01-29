''' UTILIZANDO A FUNÇÃO "FACTORIAL" DO MÓDULO MATH

from math import factorial

n = int(input('Digite um número: '))

fat = factorial(n)

print('O fatorial de {} é {}.'.format(n, fat))

'''

# Fazendo o mesmo programa com WHILE:

print('=' * 23)
print('\33[1;31mCALCULADORA DE FATORIAL\33[m')
print('=' * 23, '\n')

n = int(input('Digite um número: '))

c = n
fat = 1

print('Calculando {}! = '.format(n), end = ' ')

while c >= 1:
  
  fat *= c

  print(c, end = ' ')
  print('x' if c > 1 else '=', end = ' ')

  c -= 1

print('\33[34m', fat)
