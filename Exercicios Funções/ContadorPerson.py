'''Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros, início, fim e passo e realize a contagem através da função criada.

a) De 1 até 10 de 1 em 1;
b) De 10 a 0 de 2 em 2;
c) Uma contagem personalizada. (deverá funcionar de todas as maneiras, inicio > fim, inicio < fim, passo positivo, passo negativo.])

'''
from time import sleep

def contador(i, f, p):
  if p < 0:
    p = p*(-1)
  if i < f:
    for n in range(i, f+1, p):
      print(f'{n}', end=' ', flush=True)
      sleep(1)
  else:
     for n in range(i, f+1, -p):
      print(f'{n}', end=' ', flush=True)
      sleep(1)
  print('FIM')

# Programa Principal
  
contador(i = int(input('Digite o início: ')), f = int(input('Digite o fim: ')), p = int(input('Digite o passo: ')))

