'''Dicionários: Listas com possibilidades de índices literais ao invés de apenas números.


* O método ".append" não funciona. Adicionamos elementos diretamente pelo índice literal. 

''' 

# Declarando:
alunos = {}
# ou 
# alunos = dict()

# Atribuindo índices (keys) com os seus valores (values)
alunos['nome'] = 'Maria'

print(alunos)

alunos['idade'] = 25

print(alunos)

alunos['serie'] = 3

print(alunos)

print()

# Mostrando o valor de cada chave(key) do dicionário:
print(alunos['nome'])
print(alunos['idade'])
print(alunos['serie'])

print()

# Mostrando os valores de todos os itens, chaves(keys) e valores(values) do dicionário:
print(alunos.items())

#Mostrando apenas as chaves(keys) do dicionário:
print(alunos.keys())

# Mostrando apenas os valores das chaves do dicionário.
print(alunos.values())

print()

# Alterando o valor de uma chave do dicionário:
alunos['nome'] = 'Joaquim'
print(alunos)

print()

# Deletando uma chave(key):
# del(alunos['serie'])
# print(alunos)

print()

# Usando laços para mostrar os itens do dicionário:
for c in alunos.items():
  print(c)

print()

for c in alunos.keys():
  print(c)

print()

for c in alunos.values():
  print(c)

       
print()

for k, v in alunos.items():
  print(f'A chave {k} é igual a {v}')

print()





