''' Crie um programa que leia a idade de um atleta e mostre a sua categoria:

- Até 9 anos: MIRIM
- 14 anos: INFANTIL
- 19 anos: JUNIOR
- 20 anos: SENIOR
- Acima: MASTER

'''

idade = int(input('Digite a idade do atleta: '))

if idade<= 9:
  print('Categoria MIRIM')

elif idade > 9 and idade <= 14:
  print('Categoria INFANTIL')

elif idade > 14 and idade <= 19:
  print('Categoria JUNIOR')

elif idade == 20:
  print('Categoria SENIOR')

else:
  print('Categoria MASTER')

