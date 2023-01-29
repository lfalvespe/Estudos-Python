''' Crie um programa que leia 3 valores e diga:

1 - Se podem formar ou não um triângulo.

2 - Em caso afirmativo informe se o triângulo é:

Equilátero, isósceles ou escaleno.

'''

a = int(input('Digite o primeiro lado: '))
b = int(input('Digite o segundo lado: '))
c = int(input('Digite o terceiro lado: '))

if a >= b + c or b >= a + c or c >= a + b:
  print('{}, {} e {} não podem formar um triângulo!'.format(a, b, c))

else:
  if a == b == c:
    print('Seu triângulo é EQUILÁTERO.')

  elif a == b and a!= c:
    print('Seu triângulo é ISÓSCELES.')
  
  else:

    print('Seu triângulo é ESCALENO.')
    






