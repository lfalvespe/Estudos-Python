'''Faça um programa que leia nome e peso de várias pessoas guardando tudo numa lista. No final mostre:

a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) uma listagem com as pessoas mais leves
'''
lista = list()
lista_temp = list()
maior = menor = 0

o = ''

while True:
  lista_temp.append(str(input('Digite o nome do paciente: ')).strip().capitalize())
  lista_temp.append(int(input('Digite o peso do paciente: ')))

  if len(lista) == 0:
    maior = menor = lista_temp[1]
  else:
    if lista_temp[1] > maior:
      maior = lista_temp[1]
    if lista_temp[1] < menor:
      menor = lista_temp[1]
  
  lista.append(lista_temp[:])
  lista_temp.clear()
  o = str(input('Que continuar? [S/N]:'))

  if o in 'Nn':
    break

  
print(lista)
print('\n')

print(f'Ao todo foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi {maior}KG de: ', end = '')

for paciente in lista:
  if paciente[1] == maior:
    print(paciente[0], end=' ')

print(f'\nO menor peso foi {menor}KG de: ', end = ' ')

for paciente in lista:
  if paciente[1] == menor:
    print(paciente[0], end=' ')