'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final mostre oum boletim contendo a média de cada um e permita que o usuário possa mostra as notas de cada aluno individualmente.'''

turma = list()
o = 's'
while True:
  
  nome = str(input('Nome do aluno: '))
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  media = (nota1+nota2)/2
  turma.append([nome, [nota1, nota2], media])

  o = str(input('Quer continuar? [S/N]: '))

  if o in 'Nn':
    break

print('-='*20)
print(f'{"N°":<4} {"NOME":<17} {"MÉDIA":>4}')

for i,aluno in enumerate(turma):
  print(f'{i:<4} {aluno[0]:<18} {aluno[2]:>.1f}')

print('-='*20)

while True:
  r = int(input('Quer ver a nota de qual aluno? (999 pára) :'))

  if r == 999:
    print('FIM')
    break

  if r <= len(turma) - 1:
    print(f'Nota de {turma[r][0]}: {turma[r][1]}')

