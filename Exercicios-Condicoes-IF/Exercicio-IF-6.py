'''Crie um programa e que leia 3 números e diga qual dele é o maior e qual é o menor.'''

n1 = int(input('Digite o 1o número: '))

maior = n1
menor = n1

n2 = int(input('Digite o 2o número: '))

if n2 > n1:
  maior = n2
else:
  menor = n2

n3 = int(input('Digite o 3o número: '))

if n3 > maior:
  maior = n3
elif n3 < menor:
  menor = n3

print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
  



