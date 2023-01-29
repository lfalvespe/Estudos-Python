''' Crie um programa que leia a idade e o sexo de várias pessoas perguntando se o usuário quer continuar. No final mostre:

a) Quantas pessoas tem mais de 18 anos;
b) Quantos homens foram cadastrados;
c) Quantas mulheres tem menos de 20 anos.

'''
mais18 = 0
mmenor20 = 0
homens = 0
o = 'S'
sexo = ' '
idade = 0.6

while o in 'Ss':

    
  idade = int(input('Digite a idade: '))
  
  while sexo not in 'MmFm':
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
  
  if sexo == 'M':
    homens += 1
  if idade > 18:
    mais18 += 1
  elif idade < 20 and sexo == 'F':
    mmenor20 += 1

  sexo = ' '
  o = ' '
  while o not in 'SsNn':
    o = str(input('\nQuer continuar? [S/N]: ')).upper().strip()
 
  
print(f'\nForam cadastradas {mais18} pessoas maiores de 18 anos')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mmenor20} mulheres com menos de 20 anos\n')


    
  

