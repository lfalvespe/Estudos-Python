def cadastro():
  aluno = dict()
  turma = list()

  while True:
  
    nome = str(input('Digite o nome: ')).strip().capitalize()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: ')).strip().capitalize()
    
    aluno['nome'] = nome
    aluno['idade'] = idade
    aluno['sexo'] = sexo
    turma.append(aluno.copy())
    aluno.clear()
    r = str(input('Quer cadastrar outro aluno? [S/N]'))
    if r in 'Nn':
      break
      
  return(turma)
  
turma = cadastro()
print(turma)
  




  

