'''Crie um programa com os 20 primeiros colocados da tabela do campeonato brasileiro. Mostre no final

a) Os 5 primeiros colocados;
b) Os 4 últimos colocados;
c) Os times em ordem alfabética.
d) A posição da Chapecoense na tabela.
'''

bras = ('Atlético Mineiro', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Flamengo', 'Santos', 'Bragantino', 'Internacional', 'São Paulo', 'Ceará', 'América-MG', 'Fluminense', 'Sport', 'Cuiabá', 'Juventude', 'Grêmio', 'Atlético-PR', 'Bahia', 'Atlético-GO', 'Chapecoense')

# 5 primeiros colocados:

print('5 primeiras posições:\n')
for c,time in enumerate(bras[:5]):
  print(f'{c+1}° colocado: {bras[c]}')

# Times nas 4 últimas posições:
  
print('\nRebaixados:\n')

for d in range(len(bras)-4, len(bras)):
  print(f'{d} Colocado: {bras[d]}')

# Time em ordem alfabética:
  
ordbras = sorted(bras)

print('\nTimes em ordem alfabética:\n')
for time in ordbras:
  print(time)

# Posição da chapecoense na tabela:
print('\nColocação da Chapecoense: ', end='')
print(bras.index('Chapecoense')+1)
