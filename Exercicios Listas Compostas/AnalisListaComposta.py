
turma = list()
lista_temp = []

maiores18 = menores18 = 0
maisvelho = maisnovo = ''

for c in range(0,5):
  lista_temp.append(str(input('Digite o nome do aluno: ')))
  lista_temp.append(int(input('Digite a idade do aluno: ')))
  turma.append(lista_temp[:])
  lista_temp.clear()

for i, aluno in enumerate(turma):
  if i == 0:
    maisvelho = maisnovo = turma[i][0]
    maioridade = menoridade = turma[0][1]
  else:
    if turma[i][1] > maioridade:
      maioridade = turma[i][1]
      maisvelho = turma[i][0]
    if turma[i][1] < menoridade:
      menoridade = turma[i][1]
      maisnovo = turma[i][0]
    
  if turma[i][1] >= 18:
    maiores18 +=1
  else:
    menores18 += 1
    
  print(f'O aluno {turma[i][0]} tem {turma[i][1]} anos de idade.')

print(f'Temos {maiores18} alunos maiores de 18 anos e {menores18} alunos menores de idade.')

print(f'O aluno mais novo é {maisnovo} que tem {menoridade} anos.')
print(f'O aluno mais velho é {maisvelho} que tem {maioridade} anos.')