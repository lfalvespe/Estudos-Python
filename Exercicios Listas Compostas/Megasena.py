'''Crie um programa que pergunte ao usuário quantos jogos da megasena ele quer sortear. O programa deve gerar em cada jogo 6 números aleatórios entre 0 e 60 para cada jogo cadastrando tudo numa lista composta.'''

from random import randint
from time import sleep

jogos = list()
palpite = list()

print('-='*18)
print(f'{"Gerador de Jogos da MEGASENA":^36}')
print('-='*18)
j = int(input('- Quantos jogos você quer sortear? '))
print('\nGerando Palpites...')
print('-='*9)
print()

for c in range(0, j):
  while len(palpite) != 6:
    n = randint(1, 61)
    if n not in palpite:
      palpite.append(n)
  palpite.sort()
  jogos.append(palpite[:])
  palpite.clear()
  print(f'Palpite {c+1}: {jogos[c]}')
  sleep(2)
  

