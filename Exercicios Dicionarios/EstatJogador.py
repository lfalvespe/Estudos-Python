'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Em seguida vai ler o número de gols que ele marcou em cada partida. No final tudo isso vai ser guardado em um dicionário, incluindo o total de gols feitos no campeonato.
'''

jogador = {}
gols = list()
tot = 0

jogador['nome'] = str(input('Nome do jogador: '))

jogador['partidas'] = int(input('N° de partidas disputadas: '))

for i in range(0, jogador['partidas']):  

  n = (int(input(f'Quantos gols na {i+1} partida? ')))
  tot += n
  gols.append(n)
  
jogador['gols'] = gols.copy()
jogador['total'] = tot

print('-='*26)
print(jogador)
print('-='*26)

for k, v in jogador.items():
  print(f'{k}: \033[32m{v}\033[m')

print('-='*26)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')

for i, g in enumerate(jogador['gols']):
  print(f'=> Na partida {i+1}, fez \033[31m{g}\033[m Gols. ')

print(f'\nTotal de gols marcados: \033[33m{jogador["total"]}\033[m')

  



