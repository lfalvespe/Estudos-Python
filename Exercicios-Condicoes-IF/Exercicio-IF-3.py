'''Crie um programa que leia um número inteiro e mostre se ele é par ou impar.'''

n = int(input('Digite um número: '))

if n%2 == 0:
  print('{} é par'.format(n))

else:
  print('{} é impar'.format(n))
