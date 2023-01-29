'''Crie um programa onde o usuário possa digitar 5 valores e cadastre-os numa lista já na posição correta de inserção.

Sem usar o sort()
'''

valores = []

for c in range(0, 5):
  n = int(input('Digite um valor: '))

  if c == 0 or n > valores[-1]:
    valores.append(n)
    print('Valor adicionado no final da lista.')
  else:
    d = 0
    while d < len(valores):
      if n <= valores[d]:
        valores.insert(d, n)
        print(f'Valor adicionado na posição {d}')
        break
      d += 1

print(f'Você digitou os valores {valores}')

  
      
    