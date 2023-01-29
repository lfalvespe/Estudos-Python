'''Crie um programa que leia o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250,00 aumento de 10% e para salários iguais ou inferiores a R$ 1250, aumento de 15%.'''

sal = float(input('Digite o seu salário (R$): '))

if sal > 1250:
  aum = sal * 0.1

else:
  aum = sal * 0.15

novosal = sal + aum

print('Seu salário com aumento será R$ {}'.format(novosal))