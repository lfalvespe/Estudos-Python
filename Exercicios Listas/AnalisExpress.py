'''Crie um programa onde o usuário digita uma expressão matemática qualquer que use parênteses. O programa deverá analisar se a expressão está com os parênteses abertos e fechados na ordem correta.'''

express = str(input('Digite uma expressão matemática com parênteses: ')).strip()

pilha = list()

for caract in express:
  if caract == '(':
    pilha.append(caract)
  elif caract == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(')')
      break

if len(pilha) == 0:
  print('Sua expressão está correta')
else:
  print('Sua expreesão tem erro na disposição   dos parênteses !!!')