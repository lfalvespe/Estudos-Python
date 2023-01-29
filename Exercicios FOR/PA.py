''' Crie um programa que leia o primeiro termo e a razão de uma PA e mostre os 10 primeiro termos.'''


a1 = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a razão da PA: '))

print(a1)

for n in range(1, 10):
  
  an = a1 + n*r
  print(an)

