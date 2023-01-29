from random import randint
import os

v = 0

while True:
  print('='*25)
  print('Vamos Jogar Par ou Ímpar:')
  print('='*25)
  
  j = int(input('\nDiga um valor entre 0 e 5: '))
  c = randint(1, 5)

  poi = str(input('Par ou ímpar? [P/I]: ')).upper().strip()

  if (j + c) % 2 == 0 and poi == 'P' or (j + c) %2 != 0 and poi == 'I':

    v += 1
    os.system('clear')
    print(f'\nComputador: {c} \nJogador: {j} \nResultado: {c+j} \n\nVocê venceu !!! \n')
    
  else:
    print(f'\nComputador: {c} \nJogador: {j} \nResultado: {c+j} \n\nFim de jogo, Você Perdeu !!! \n')
    break
    os.system('clear')

print(f'Nº de vitórias: {v}')
  
