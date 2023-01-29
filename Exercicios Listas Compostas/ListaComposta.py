# LISTAS dentro de LISTAS

aluno1 = ['Maria', 20, 'Recife']
aluno2 = ['João', 33, 'Olinda']
aluno3 = ['Ana', 19, 'Jaboatão']
aluno4 = ['Paula', 18, 'Paulista']

turma = list()

turma.append(aluno1[:])
turma.append(aluno2[:])
turma.append(aluno3[:])
turma.append(aluno4[:])

print(turma)
print('\n')

print(turma[0])
print('\n')

print(turma[0][0])
print('\n')

print(turma[0][1])
print('\n')

print(turma[0][2])
print('\n')

for c, aluno in enumerate(turma):
  print(f'\nAluno: {turma[c][0]}')
  print(f'Idade: {turma[c][1]}')
  print(f'Cidade: {turma[c][2]}')


  




