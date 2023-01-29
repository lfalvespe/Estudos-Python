def par(n = 0):
  if n % 2 == 0:
    return True
  else:
    return False

n = int(input('Digite um número: '))
if par(n):
  print('É par')
else:
  print('É ímpar')