num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

o = 'S'

while o == 'S':

  while True:

    n = int(input('Digite um número: '))

    if 0 <= n <= 20:
      break
    else:
      print('Tente novamente. ', end = '')
  print(f'Você digitou o número {num[n]}')

  o = str(input('Quer continuar? [S/N]: ')).upper().strip()

