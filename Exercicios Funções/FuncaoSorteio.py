'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar(). A primeira função vai sortear 5 números e colocá-los dentro da lista e a segunda função vai mostra a soma entre todos os valores pares sorteados pela fnção anterior.'''

from random import randint
from time import sleep


def sorteia():
  lista = []
  i = 0

  print('Sorteando 5 valores da lista: ', end=' ')
  while i < 6:
    lista.append(randint(1, 10))
    print(lista[i], end=' ', flush=True)
    sleep(0.5)
    i += 1
  return(lista)

def somapar(numeros):
  s = 0
  for n in numeros:
    if n % 2 == 0:
      s += n
  print(f'\nSomando os valores pares de {numeros}, temos {s}')
  
  
#Programa Principal
somapar(sorteia())