"""Crie um programa que escolha um número inteiro de 1 até 5 e peça para o usuário adivinhar. Diga se ele acertou ou errou.
"""

import random

n = random.randint(0, 10)

x = int(input('Digite um número: '))

print('Meu número: {}\nSeu número: {}'.format(n, x))

if x == n:
  print('VOCÊ ACERTOU')

else:
  print('VOCÊ ERROU')


