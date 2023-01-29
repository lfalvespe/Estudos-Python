'''Faça um programa que tenha uma função chamada area(). Que receba as dimensões de um terreno retangular e mostre a área do terreno'''

def area(c, l):
  a = c*l
  print(f'A área de um terreno de {c} x {l} vale {a}m²')

area(c = float(input('Comprimento: ')), l = float(input('Largura: ')))
