# Colocando um dicionário dentro de uma lista

aluno1 = {'nome': 'João', 'idade': 22, 'sexo': 'M'}
aluno2 = {'nome': 'Maria', 'idade': 18, 'sexo': 'F'}
aluno3 = {'nome': 'Pedro', 'idade': 31, 'sexo': 'M'}

turma = list()

# [:] não funciona com dicionários. Usamos o método .copy()
turma.append(aluno1.copy()) 
turma.append(aluno2.copy())
turma.append(aluno3.copy())

print(turma)

print()

print(turma[0]['nome'])
print(turma[1]['idade'])
print(turma[2]['idade'])
print(turma[2]['sexo'])

print()

for aluno in turma:
  print(f'O aluno {aluno["nome"]} do sexo {aluno["sexo"]} tem {aluno["idade"]} anos.')