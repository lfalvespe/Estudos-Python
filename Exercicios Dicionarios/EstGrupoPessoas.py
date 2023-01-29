'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre:

a) Quantas pessoas foram cadastradas;
b) A média de idade do grupo;
c) Uma lista com todas as mulheres;
d)Uma lista com todas as pessoas com idade acima da média.

'''

o = 's'
pessoa = {}
lista = []
soma = 0

while True:
  pessoa['nome'] = str(input('Digite o nome: ')).strip().capitalize()
  pessoa['sexo'] = str(input('Digite o sexo [M/F]')).strip().upper()
  pessoa['idade'] = int(input('Digite a idade: '))
  soma += pessoa['idade']
  lista.append(pessoa.copy())
  pessoa.clear()
  
  o = str(input('Quer continuar? [S/N]: '))
  if o in 'Nn':
    break
media = soma/len(lista)
print('-='*15)
print(f'- O grupo tem {len(lista)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos')

print('- As mulheres do grupo são: ', end ='')
for pessoa in lista:
  if pessoa['sexo'] == 'F':
    print(pessoa["nome"], end=' ')

print('\n- Lista de pessoas acima da média: ')
print()

for pessoa in lista:
  if pessoa['idade'] > media:
    print(pessoa)
  
  
  
  