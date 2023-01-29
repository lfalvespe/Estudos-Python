a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite o segundo termo da PA: '))

an = a1
c = 1
o = 1
termos = 10

while o != 0:
  
  while c <= termos:
    print('{} -> '.format(an), end = '' )
    an += r
    c += 1

  print('Pausa')

  o = int(input('Quer ver mais quantos termos? '))
  
  c = 1
  termos = o

print('FIM')