'''Faça um programa que leia nome e média de um aluno guardando também a sua situação em um dicionário. Ao final mostre o conteúdo da estrutura.'''

aluno = dict()

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a média do aluno: '))

if aluno['media'] >= 7:
  aluno['situacao'] = 'Aprovado'
else:
  aluno['situacao'] = 'Reprovado'

print(f'O aluno {aluno["nome"]} teve média {aluno["media"]} e está {aluno["situacao"]}')