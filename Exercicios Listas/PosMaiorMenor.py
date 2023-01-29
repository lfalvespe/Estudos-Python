'''Crie um programa que leia 5 valores numéricos e guarde numa lista. No final mostre:

O maior e o menor valor e suas respectivas posições.
'''

lista = []
maior = menor = 0
posmenor = posmaior = 0

for c in range(0, 5):
  lista.append(int(input(f'Digite o {c+1}° Valor:  ')))
  
  if c == 0:
    menor = lista[c]
    maior = lista[c]
  