

turma = list()
aluno = list()
notas = list()
o = 's'

nota1 = 0
nota2 = 0

while True:
  nome = str(input('Nome do aluno: ')).strip().capitalize()
  nota1 = float(input('Nota 1: '))
  notas.append(nota1)
  nota2 = float(input('Nota 2: '))
  notas.append(nota2)
  media = (nota1+nota2)/2
  aluno.append(nome)
  aluno.append(notas[:])
  aluno.append(media)
  turma.append(aluno[:])
  notas.clear()
  aluno.clear()
  
  o = str(input('Quer continuar? [S/N]')).strip()
  if o in 'Nn':
    break

print('-='*15)

print(f'{"Nº":<3} {"NOME":<20} {"MÉDIA":>}')

for i in range(0, len(turma)):
  print(f'{i:<3} {turma[i][0]:<20} {turma[i][2]:>}')

print('-='*15)


while True:
  a = int(input('Mostrar notas de qual aluno? (999 interrompe: '))
  if a == 999:
    break
  print(f'Notas de {turma[a][0]}: {turma[a][1]}')


