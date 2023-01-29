''' Crie um programa que mostre a tabuada do número que o usuário quiser ver'''

n = int(input('Quer ver a tabuada de qual número? '))

for i in range(11):
  print('{} x {} = {}'.format(n, i, n*i))