'''Faça um programa que tenha uma função chamada ficha, que receba dois parâmetros opcionais, o nome de um jogador e a quantidade de gols marcados. O programa deverá ser capaz de mostrar a ficha do jogador mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(nome='<Desconhecido>', gols='0'):

  print(f'\nO jogador {nome} marcou {gols} gols.')

#programa principal

n = str(input('Digite o nome do jogador: ')).strip().capitalize()
g = str(input('Digite o nº de gols marcados: '))
if g.isnumeric():
  g = int(g)
else:
  g = 0
if n == '':
  ficha(gols = g)
else:
  ficha(n, g)
  
  