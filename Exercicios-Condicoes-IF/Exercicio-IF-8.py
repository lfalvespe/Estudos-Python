'''Crie um programa que leia os 3 números inteiros e diga se eles formam ou não um triângulo.'''

a = int(input('Digite o 1o lado: '))
b = int(input('Digite o 2o lado: '))
c = int(input('Digite o 3o lado: '))

if a >= b+c or b >= a+c or c >=a+b:
  print('{}, {} e {} não formam um triângulo'.format(a, b, c))

else:
   print('{}, {} e {} formam um triângulo'.format(a, b, c))