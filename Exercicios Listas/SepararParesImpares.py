'''Crie um programa que leia vários valores e cadastre-os numa lista. Ao final mostre>

a) Quantos valores foram digitados.
b) a lista de valores ordenada de forma decrescente.

c) se o valor 5 foi digitado.

'''
lista = []
pares = []
impares = []

while True:
  lista.append(int('Digite um valor: '))
  o = str(input('Quer continuar? [S/N] ')).strip()
  if o in 'Nn':
    break
    
for c in range(0, len(lista)):
  if lista[c] % 2 == 0:
    pares.append(lista[c])
  else:
    impares.append(lista[c])

print(f'Valores digitados: {lista}')
print(f'Valores pares digitados {pares}')
print(f'Valores ímpares digitados: {impares}')
