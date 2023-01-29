"""Crie um programa que leia a velocidade de um carro. Se o carro ultrapassar 80 km/h mostre a mensagem que foi multado. Nesse caso mostre o valor da multa que será de R$ 7,00 por cada Km/h ultrapassado do limite. """

v = float(input('Digite a velocidade do veículo (KM/H): '))

if v <= 80:
  print('Parabéns, Você respeita os limites de velocidade!')

else:

  m = (v - 80) * 7
  
  print('Você foi multado por ultrapassar em {} km/h a velocidade máxima permitida.'.format(v-80))
  print('Valor da multa: R$ {}'.format(m))
  