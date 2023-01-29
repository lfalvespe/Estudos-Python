''' Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero a 20. O programa deverá ler um número de 0 a 20 pelo teclado e mostrálo por extenso'''

num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

o = 's'

while o in 'Ss':

  while True:
    n = int(input('Digite um número: '))

    if 0 <= n <= 20:
      break
    print('Tente novamente. ', end = ' ')
  print(f'Você digitou o número {num[n]}')

  o = str(input('Quer continuar? [S/N]: '))