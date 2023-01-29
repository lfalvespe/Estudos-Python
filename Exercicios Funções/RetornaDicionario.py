'''Crie um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguntes informações:

A) Quantidade de notas.
b) A maior nota.
c) A menor nota.
d) A média da turma.
e) A situação(Opcional)
'''

def notas(*num, sit =False):
  '''
  - Função Notas():
  - n1, n1, ... (float)
  - sit (Boolean) - Mostra ou oculta a situação.
  '''
  n = (num[:])
  resultados = dict()
  resultados['total'] = len(n)
  resultados['maior'] = max(n)
  resultados['menor'] = min(n)
  resultados['media'] = sum(n)/len(n)
  
  if sit:
    
    if resultados['media'] < 6:
      resultados['situacao'] = 'ruim'
    else:
      resultados['situacao'] = 'Boa'
    
  
  print(resultados)
  
# Progrma principal
  
notas(3, 4, 6, 8, 6, 1, sit = True)


print()

help(notas)