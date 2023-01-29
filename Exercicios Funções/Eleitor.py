'''Crie um programa que tenha uma função chamada voto(). Que vai receber como parâmetro o ano de nascimento de uma pessoa retornando um valor literal indicando se uma pessoa tem voto Negado, Opcional ou Obrigatório nas eleições.'''

def voto(nasc):
  from datetime import date
  
  idade = date.today().year - nasc
  if idade < 18:
    return f'Com {idade} anos, Voto Negado!'
  elif 18 <= idade < 65:
    return f'Com {idade} anos, Voto Obrigatório.'
  else:
    return f'Com {idade} anos, Voto Opcional.'

situacao = voto((int(input('Digite o ano de nascimento: '))))
print(situacao)



      