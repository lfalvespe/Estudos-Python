'''Crie um programa que leia nome, ano de nascimento e CTPS de uma pessoa e cadastre-os (com idade) em um dicionário. Se a CTPS for diferente de zero, receba também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date

contrib = dict()

contrib['Nome'] = str(input('Digite seu nome: ')).strip().capitalize()
ano_nasc = int(input('Digite o ano de nascimento: '))
contrib['Idade'] = date.today().year - ano_nasc
contrib['CTPS'] = int(input('Digite sua CTPS [0 se não possui CTPS]: '))

if contrib['CTPS'] == 0:
  for k, v in contrib.items():
    print(f'{k} = {v}')
  print('Contribuinte não possui CTPS.')
else:
  contrib['Ano_contrat'] = int(input('Digite o ano de contratação: '))
  contrib['Salario'] = int(input('Digite seu salário: '))
  Temp_contrib = date.today().year - contrib['Ano_contrat']

  TempParaApos = 35 - Temp_contrib
  contrib['Idade_apos'] = contrib['Idade'] + TempParaApos
  for k, v in contrib.items():
    print(f'{k}: {v}')

  print(f'\nvocê irá se aposentar com {contrib["Idade_apos"]} anos.')

contrib.items