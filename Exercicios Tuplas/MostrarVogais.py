'''Crie um programa que tenha uma tupla com várias palavras sem acentos. Mostrar em cada palavra quais são as suas vogais.'''

palavras = ('Arvore', 'Mercado', 'Padaria', 'Eletrodoméstico', 'Periferia', 'Estadual', 'Preferivelmente')


for p in palavras:
  print(f'\nVogais em {p.upper()}: ', end = '')
  for vogal in p:
    if vogal.lower() in 'aeiou':
      print(vogal.lower(), end = ' ')


# outra forma:

'''
for c in range(0, len(palavras)):
  print(f'\nVogais em {palavras[c].upper()}: ', end = '')
  for d in palavras[c]:
    if d in 'aeiou':
      print(d, end = ' ')

'''