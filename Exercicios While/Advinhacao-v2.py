import random

r = -1
tent = 0

n = random.randint(1, 11)

while r != n:
  r = int(input('Em qual número estou pensando? '))
  tent += 1

print('Você acertou', r)
print('No de tentativas: ', tent)

