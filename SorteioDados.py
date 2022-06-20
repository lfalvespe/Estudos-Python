'''Crie um programa onde 4 jogadores joguem dados e obtenham resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem. Sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(1, 6), 
             'jogador2': randint(1, 6), 
             'jogador3': randint(1, 6), 
             'jogador4': randint(1, 6)}


print('Valores sorteador:')
print()
for j in jogadores:
  print(f'O {j} tirou {jogadores[j]}')
  sleep(1)

ranking = list()

ranking = (sorted(jogadores.items(), key=itemgetter(1), reverse=True))

print('-='*11)
print('Ranking dos jogadores:')

print()

for i, jog in enumerate(ranking):
  print(f'{i+1}° Lugar: {jog[0]} com {jog[1]} pontos')
  

