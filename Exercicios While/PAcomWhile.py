a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite o segundo termo da PA: '))

c = 0

while c < 10:
  a = a1 + c*r

  c += 1
  
  print(a, end = ' ')