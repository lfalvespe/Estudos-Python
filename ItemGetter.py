# Módulo operator

from operator import itemgetter

''' Para colocar um dicionário em ordem de acordo com a chave escolhida.

Ex.:

'''
jogadores = {'jogador1': 3, 
             'jogador2': 5, 
             'jogador3': 1, 
             'jogador4': 2}

ranking = list()

ranking = (sorted(jogadores.items(), key=itemgetter(1), reverse=True))

for i, jog in enumerate(ranking):
  print(f'{i+1}° Lugar: {jog[0]} com {jog[1]} pontos')