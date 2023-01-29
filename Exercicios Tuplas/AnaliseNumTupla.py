'''Crie um programa que leia 4 valores pelo teclado e guarde-os em uma Tupla. Mostre:

a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.

'''
a1 = int(input('Digite um número: '))
a2 = int(input('Digite outro número: '))
a3 = int(input('Digite mais um número: '))
a4 = int(input('Digite o último número: '))

tupla = (a1, a2, a3, a4)

print(f'\nVocê digitou os números: {tupla}')

print(f'O número 9 foi digitado {tupla.count(9)} vez(es).')

if 3 in tupla:
  print(f'O número 3 apareceu primeiro na posição {tupla.index(3)+1}.')
else:
  print('O número 3 não foi digitado nenhuma vez.')

print('Os números pares digitados foram: ', end = '')
for pares in tupla:
  if pares % 2 == 0:
    print(pares, end = ' ')

  