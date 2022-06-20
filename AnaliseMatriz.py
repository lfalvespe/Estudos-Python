'''Cria r uma matriz 3x3 com os valores lidos pelo teclado, exibir a matriz e também:

a) A soma dos valores pares.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = 0
somacoluna3 = 0
maiorlinha2 = 0


for l in range(0, 3):
  for c in range(0, 3):
    matriz[l][c] = int(input(f'Digite o termo ({l},{c}): '))

for l in range(0, 3):
  for c in range(0, 3):
    if matriz[l][c] % 2 == 0:
      somapares += matriz[l][c]

    if c == 2:
      somacoluna3 += matriz[l][c]

    if l == 1:
      if maiorlinha2 < matriz[l][c]:
        maiorlinha2 = matriz[l][c]

print('-='*30)

for l in range(0, 3):
  for c in range(0, 3):
    print(f'{matriz[l][c]:^5}', end='')
  print()

print('-='*30)

print(f'A soma dos termos pares da matriz é: {somapares}')
print(f'A soma dos valores da terceira coluna é: {somacoluna3}')
print(f'O maior valor da segunda linha é {maiorlinha2}')

    


