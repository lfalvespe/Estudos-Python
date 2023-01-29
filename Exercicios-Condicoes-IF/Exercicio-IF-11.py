''' Escreva um programa que leia dois números, compare-os e informe uma das seguintes mensagens

- O primeiro valor é maior.
- O segundo valor é maior
- Não existe valor maior. Os dois são iguais.
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
  print('O primeiro valor é maior')
elif n1 < n2:
  print('O segundo valor é maior')
else:
  print('Não existe valor maior. Os dois são iguais')

