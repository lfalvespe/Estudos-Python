'''Faça um programa que crie um amatriz de dimensão 3x3 e preencha com valores do teclado.'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]

for l in range(0, 3):
  for c in range(0, 3):
    matriz[l][c] = (int(input(f'Digite o termo ({l}, {c}): ')))

print(matriz)

for l in range(0, 3):
  for c in range(0, 3):
    print(f'{matriz[l][c]:^5}', end = '')
  print()

