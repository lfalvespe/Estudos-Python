'''Crie um programa que tenha uma função chamada fatorial que receba dois parâmetros. O primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(n = 1, show=True):
  '''
  => Calcula o fatorial de um número.
  (int) n: número para cálculo do fatorial.
  (bool) show: mostra o cálculo (opcional)
  '''
  
  fat = 1
  c = n

  ''''''
  while c > 0:
    if show:
      print(c, end='')
      if c > 1:
        print('x', end='')
      else:
        print('=', end='')
    fat *= c
    c -= 1
  return fat


# Programa principal

n = int(input('Digite um número: '))
f = fatorial(n)
print(f)


print()

help(fatorial)