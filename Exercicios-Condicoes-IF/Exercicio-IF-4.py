''' Crie um programa que leia a distância de uma viagem e calcule o preço da passagem cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 por km para viagens mais longas.'''

d = float(input('Digite a distância da viagem em km: '))

if d <= 200:
  p = d * 0.50
  print('O preço da sua passagem é: R$ {}'.format(p))
  
else:
  p = d * 0.45
  print('O preço da sua passagem é: R$ {}'.format(p))

