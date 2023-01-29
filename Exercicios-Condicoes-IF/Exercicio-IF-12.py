''' Escreva um programa que leia o ano de nascimento de um rapaz e informe

- Se ele ainda vai se alistar ao serviço militar.
- Se já é hora de ele se alistar.
- Se já passou do tempo de alistamento.
- O tempo que falta ou o tempo que passou do prazo.
'''

from datetime import date

nasc = int(input('Digite o ano do seu nascimento: '))

idade = date.today().year - nasc

if idade < 18:
  tempo = 18 - idade
  print('Você ainda vai se alistar ao serviço militar.')
  print('Falta(m) {} ano(s)'.format(tempo))

elif idade > 18:
  tempo = idade - 18
  print('Você já ultrapassou o tempo de alistamento militar')
  print('Você está {} anos atrasado.'.format(tempo))

else:
  print('É hora de você se alistar ao serviço militar')




